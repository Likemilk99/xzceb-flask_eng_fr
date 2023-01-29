import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    if englishText is None:
        return None

    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result().get("translations")[0].get("translation")

    return frenchText


def frenchToEnglish(frenchText):
    if frenchText is None:
        return None

    englishText = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result().get("translations")[0].get("translation")

    return englishText
