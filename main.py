from google.cloud import translate
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config['auth']['credential_path']

def sample_translate_text(text, target_language, project_id):
    """
    Translating Text
    Args:
      text The content to translate in string format
      target_language Required. The BCP-47 language code to use for translation.
    """

    client = translate.TranslationServiceClient()

    # TODO(developer): Uncomment and set the following variables
    text = 'Text you wish to translate'
    target_language = 'ja'
    project_id = 'ai-writer-275301'
    contents = [text]
    parent = client.location_path(project_id, "global")

    response = client.translate_text(
        parent=parent,
        contents=contents,
        mime_type='text/plain',  # mime types: text/plain, text/html
        source_language_code='en-US',
        target_language_code=target_language)
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))


# [END translate_v3_translate_text]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, default="Hello, world!")
    parser.add_argument("--target_language", type=str, default="fr")
    parser.add_argument("--project_id", type=str, default="[Google Cloud Project ID]")
    args = parser.parse_args()

    sample_translate_text(args.text, args.target_language, args.project_id)


if __name__ == "__main__":
    main()
