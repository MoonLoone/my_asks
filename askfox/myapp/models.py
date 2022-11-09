from django.db import models

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answers_number': question_id + 1,
        'rate': 10 - question_id,
        'tags': ['tag' + str(i) for i in range(question_id)]
    } for question_id in range(10)
]

ANSWERS = [
    [
        {
            'id': answer_id,
            'rate': 10 - question_id,
            'text': f'Text of question #{answer_id}',
        } for answer_id in range(2, 10)
    ] for question_id in range(10)
]
