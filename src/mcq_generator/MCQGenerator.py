import os
from dotenv import load_dotenv
from src.mcq_generator.utils import read_file
from src.mcq_generator.logger import logging
from langchain import PromptTemplate,LLMChain  # ascessing the llms models of openAI API by langchain framework
from langchain_huggingface import HuggingFaceEndpoint

# Importing necessary packages from langchain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("Value of MY_VARIABLE:", key)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    temperature=0.5,
    token=key
)

template = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Ensure to make {number} MCQs 
"""

logging.info("Template 1 defined")

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone"],
    template=template
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
print("Quiz chain initialized")

Template2 = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students.
You need to evaluate the complexity of the question and give a complete analysis of the quiz if the students will be able to understand the questions and answer them. Only use at max 50 words for complexity analysis.
And you should make sure don't generate this  Best regards, [Your Name] and also keep in mind that generate the mcqs in good formate and give a space between them while generating output 
Check from an expert English Writer of the below quiz:
{quiz}
"""

logging.info("Template 2 defined")

quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=Template2)

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)
print("Review chain initialized")

logging.info("Review chain defined")

# This is an Overall Chain where we run the two chains in Sequence
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "subject", "tone"],
    output_variables=["quiz", "review"],
    verbose=True,
)

print("Sequential chain initialized")

logging.info("Sequential chain defined")