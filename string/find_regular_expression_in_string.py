import re


def get_transcripts_and_predictions(decoder_response):
    try:
        transcript_strings = re.findall(r'\|T\|:.*\n', decoder_response)
        transcripts = [transcript_string[5:-1].strip() for transcript_string in transcript_strings]

        prediction_strings = re.findall(r'\|P\|:.*\n', decoder_response)
        predictions = [prediction_string[5:-1].strip() for prediction_string in prediction_strings]

        return transcripts, predictions
    except AttributeError:
        raise Exception('Unexpected response: {}'.format(decoder_response))
