from dotenv import load_dotenv
import os

import openai
import logging
from domain.services.load_parameter import load_parameters

load_dotenv()


def logic_retry_openai(**kwargs):
    """
    This is a function for retry openai.
    Args: kwargs
    Returns: response
    """
    return openai.Completion.create(**kwargs)


def login_openai() -> dict:
    """
    This is a function for  login to openai.
    """
    logging.warning("Executing login_openai")
    try:
        openai.api_key = os.getenv("AZOPENAIKEY")
        openai.api_base = os.getenv("AZOPENAIENDPOINT")
        openai.api_type = os.getenv("AZOPENAITYPE")
        openai.api_version = os.getenv("AZOPENAIVERSION")
        logging.warning("Login to openai")
        logging.error(openai.api_key)

    except Exception as e:
        print("No credentials for openai")
        print(e)


def ask_openai(prompt: str) -> dict:
    """
    This is a function for
    ask question to AZURE GPT by OpenAI.
    """
    logging.warning("Executing ask_openai")
    login_openai()
    loaded_parameters = load_parameters()
    parameters = loaded_parameters["open_ai_parameters_change"]
    # print(prompt)
    response = openai.Completion.create(
        engine=parameters["model"],
        prompt=prompt,
        temperature=parameters["temperature"],
        max_tokens=parameters["max_tokens"],
        top_p=parameters["top_p"],
        frequency_penalty=parameters["frequency_penalty"],
        presence_penalty=parameters["presence_penalty"],
        logprobs=1,
    )

    try:
        return {
            "text": response.choices[0].text.lstrip(),
            # "meanProbability": response_mean_probability,
        }
    except Exception as e:
        logging.warning("Error in ask_openai")
        logging.warning(e)
        logging.warning(response.choices)
