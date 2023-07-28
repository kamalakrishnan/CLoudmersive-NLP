from django.shortcuts import render
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint
from django.http import Http404


configuration = cloudmersive_nlp_api_client.Configuration()
configuration.api_key['Apikey'] = '8e8e859d-1138-4da1-b893-3218a8105d8c'


def index(request):
    context={}
    if request.method == 'POST':
        print(request.POST.get('operation'))

        if request.POST.get('operation') and request.POST.get('input_string'):
            if request.POST.get('operation') == 'Perform Sentiment Analysis and Classification on Text':
                result=analytics(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
            if request.POST.get('operation') == 'Part-of-speech tag a string, filter to verbs':
                result=POSverbs(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
            if request.POST.get('operation') == 'Part-of-speech tag a string, filter to nouns':
                result=POSnoun(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
            if request.POST.get('operation') == 'Part-of-speech tag a string, filter to adjectives':
                result=POSadjectives(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
            if request.POST.get('operation') == 'Translate English to German text':
                result=toGerman(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
            if request.POST.get('operation') == 'Translate English to French text':
                result=toFrench(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
            if request.POST.get('operation') == 'Rephrase English text sentence-by-sentence':
                result=rephrase(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
            if request.POST.get('operation') == 'Get words in input string':
                result=segment(request.POST.get('input_string'))
                operations=request.POST.get('operation')
                inputs=request.POST.get('input_string')
                context={'result':result, 'userinput':inputs, 'useroperation':operations}
                print(result)
        else:
            print('else called')

    return render(request, 'nlp/index.html',context)
        

def analytics(text):
    api_instance = cloudmersive_nlp_api_client.AnalyticsApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    input = cloudmersive_nlp_api_client.SentimentAnalysisRequest(text)

    # SentimentAnalysisRequest | Input sentiment analysis request
    try:
        # Perform Sentiment Analysis and Classification on Text
        api_response = api_instance.analytics_sentiment(input)
        return api_response.sentiment_classification_result
    except ApiException as e:
        return 'Exception occured. Try again.'

def POSverbs(text):
    api_instance = cloudmersive_nlp_api_client.PosTaggerApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    request = cloudmersive_nlp_api_client.PosRequest(text) # PosRequest | Input string

    try:
    # Part-of-speech tag a string, filter to verbs
        api_response = api_instance.pos_tagger_tag_verbs(request)
        words = api_response.tagged_sentences[0].words
        if len(words) == 0:
            return 'There is no verb in this sentence.'
        else:
            return words[0].word
    except ApiException as e:
        return 'Exception occured. Try again.'

def POSnoun(text):
    # create an instance of the API class
    api_instance = cloudmersive_nlp_api_client.PosTaggerApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    request = cloudmersive_nlp_api_client.PosRequest(text) # PosRequest | Input string

    try:
        # Part-of-speech tag a string, filter to nouns
        api_response = api_instance.pos_tagger_tag_nouns(request)
        words = api_response.tagged_sentences[0].words
        if len(words) == 0:
            return 'There is no noun in this sentence.'
        else:
            return words[0].word
    except ApiException as e:
        return 'Exception occured. Try again.'

def POSadjectives(text):
    # create an instance of the API class
    api_instance = cloudmersive_nlp_api_client.PosTaggerApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    request = cloudmersive_nlp_api_client.PosRequest(text) # PosRequest | Input string

    try:
        # Part-of-speech tag a string, filter to adjectives
        api_response = api_instance.pos_tagger_tag_adjectives(request)
        words = api_response.tagged_sentences[0].words
        if len(words) == 0:
            return 'There is no adjective in this sentence.'
        else:
            return words[0].word
    except ApiException as e:
        return 'Exception occured. Try again.'
def toGerman(text):
    api_instance = cloudmersive_nlp_api_client.LanguageTranslationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    input = cloudmersive_nlp_api_client.LanguageTranslationRequest(text) # LanguageTranslationRequest | Input translation request

    try:
        # Translate English to German text with Deep Learning AI
        api_response = api_instance.language_translation_translate_eng_to_deu(input)
        return api_response.translated_text_result
    except ApiException as e:
       return 'Exception occured. Try again.'

def toFrench(text):
    api_instance = cloudmersive_nlp_api_client.LanguageTranslationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    input = cloudmersive_nlp_api_client.LanguageTranslationRequest(text) # LanguageTranslationRequest | Input translation request

    try:
        # Translate English to French text with Deep Learning AI
        api_response = api_instance.language_translation_translate_eng_to_fra(input)
        return api_response.translated_text_result
    except ApiException as e:
        return 'Exception occured. Try again.'

def rephrase(text):
    api_instance = cloudmersive_nlp_api_client.RephraseApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    input = cloudmersive_nlp_api_client.RephraseRequest(text) # RephraseRequest | Input rephrase request

    try:
        # Rephrase, paraphrase English text sentence-by-sentence using Deep Learning AI
        api_response = api_instance.rephrase_english_rephrase_sentence_by_sentence(input)
        return api_response.rephrased_results[0].rephrasings[0].rephrased_sentence_text
    except ApiException as e:
        return 'Exception occured. Try again.'

def segment(text):
    api_instance = cloudmersive_nlp_api_client.SegmentationApi(cloudmersive_nlp_api_client.ApiClient(configuration))
    input = cloudmersive_nlp_api_client.GetWordsRequest(text) # SentenceSegmentationRequest | Input string
    try:
        # Extract sentences from string
        print(text)
        api_response = api_instance.segmentation_get_words(input)
        result = ', '.join(word.word for word in api_response.words)
        print(result)
        return result

    except ApiException as e:
        return 'Exception occured. Try again.'       