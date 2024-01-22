GENERATE_ESSAY_PROMPT_TEMPLATE = "Based on premise: \"{}\" generate story containing several scenes, use scene1:, scene2:, ... to represent."

RATE_ESSAY_PROMPT_TEMPLATE="Based on 1. Interesting. Interesting to the reader. 2. Coherent. Plot-coherent. 3. Relevant. Faithful to the initial premise. 4. Humanlike. Judged to be human-written.4 dimensions evaluate following 2 stories, the score is from 0 to 100, higher score means better.\nThe initial premise of story is \"{}\"\nStory 1: {}\n Story 2: {}."

HANNA_RATE_ESSAY_PROMPT_TEMPLATE="Based on the following six categories: 1. Relevance. 2. Coherence. 3. Empathy. 4. Surprise. 5. Engagement. 6. Complexity, evaluate the following two stories by assigning an integer score (from 1 to 5) to each category. Higher score means better.\nThe initial premise of story is: {}\nStory1: {}\n Story2: {}.\n\nIn your response, please use the following example format strictly and no need for any extra explanations: \nStory1\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \nStory2\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \n"

HANNA_RATE_SINGLE_ESSAY_PROMPT_TEMPLATE="Based on the following six categories: 1. Relevance. 2. Coherence. 3. Empathy. 4. Surprise. 5. Engagement. 6. Complexity, evaluate the following story by assigning an integer score (from 1 to 5) to each category. Higher score means better.\nThe initial premise of story is: {}\nStory: {}\n\nIn your response, please use the following example format strictly and no need for any extra explanations:\nRelevance: \nCoherence: \nEmpathy: \nSurprise: \nEngagement: \nComplexity: \n"

# HANNA_RATE_ESSAY_PROMPT_TEMPLATE="Based on the following four categories: 1. Interesting, 2. Coherent, 3. Relevant, 4. Humanlike, evaluate the following two stories by assigning an integer score (from 1 to 5) to each category. Higher score means better.\nThe initial premise of story is: {}\n\nStory1: {}\n\n Story2: {}.\n\nIn your response, please use the following example format strictly and no need for any extra explanations: \nStory1\nInteresting: 3\nCoherent: 4\nRelevant: 5\nHumanlike: 2\nStory2\nInteresting: 1\nCoherent: 5\nRelevant: 5\nHumanlike: 3\n"

# HANNA_RATE_ESSAY_PROMPT_TEMPLATE="Evaluate the following two stories by assigning an integer score (from 1 to 30) to each. Higher score means better.\nThe initial premise of story is: {}\n\nStory1: {}\n\n Story2: {}.\n\nIn your response, please use the following example format strictly and no need for any extra explanations: \nStory1\nScore: 19\nStory2\nScore: 22\n"


QUARREL_PREMISE = "You will collaborate to create a story. The general setting: A Quarrel between two good friends about Iron Man."
IBRUSIA_PREMISE = "You will collaborate to create a story. The general setting: The state of Ibrusia is coming to a desperate and dangerous situation as the Hosso Union approaches its capital, Zaragoza."
ECONOMY_PREMISE = "You will collaborate to create a story. The general setting: The state of Gurata is coming to a huge economic recession. People are in panic and streets are in turmoil."