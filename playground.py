import litellm
import re

from standard_prompts import *

litellm.vertex_project = "multi-agent-411823"
litellm.vertex_location = "us-central1"

# Helper function
def extract_first_number(text):
        """
        Helper function to extract the first number encountered within a string.
        """
        match = re.search(r'\d+', text)
        if match:
            return int(match.group(0))
        else:
            return None


def get_response(model, message, temperature=None, top_p=None):
    """
    Query the LLM model with a message and return the response.
    """
    response = litellm.completion(
        model=model,
        messages=[{"content": message, "role": "user"}],
        temperature=temperature,
        top_p=top_p,
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    premise = "A scientific study proves that all humans have been breathing a mind-altering gas from birth. It has been in the air since the beginning of recorded time. People have been in a constant state of being high. Until now. Specialised gas masks are handed out and people have begun to act strange."

    human_story = "When Tyler entered the ward, his daughter Valerie was already fast asleep, her frail body no match for the potent cocktail of drugs coursing through her veins. “She’s been drifting all day, so you didn’t miss much, ” said Roni as she got up to embrace her husband. “How did the appeal go? ” Tyler smiled mournfully. “No luck there. They acknowledged my potential as a Donner, but I failed the psych evaluation again. ‘ Likely to succumb to pressures from family situation’, they said. No matter, we’ll find another way to get the money we need for Valerie’s treatments.” Tyler and Roni sat quietly as they cast furtive glances at Valerie, each lost in their own thoughts. Roni was the first to break the silence. “Did they say which project you would have been assigned to if you became a Donner? ” “They did, in fact. There’s an opening on the Renewable Energies team. They think they’re on the verge of a breakthrough, and one additional Donner is all they need to beat the Chinese competitors to the patenting deadline.” Tyler sighed, then leaned back in his chair and closed his eyes before continuing, “The hazard pay was really good too. 5 years’salary for just one month of being a Donner! And full psych after-care thrown in as well! ” Roni’s grip on Tyler’s hand tightened then. “Have the suicide rates… decreased with the psych after-care? ” “That’s what they claim, at least. Some still believe that the utter desolation one experiences with the absence of Perogon-X2 is irreversible, but hey, if that’s the price for increased mental faculties, up to a 100-point increase in IQ, there’ll always be people willing to pay.” Roni fished out a print-out from her handbag, and passed it over to Tyler. “This other group believes that Perogon-X2 is a good rather than bad thing. This ‘ naturally-occurring high’, as they call it, is the only thing keeping us from falling into a spiralling abyss of depression ... it’s the proverbial wool over our eyes, but for our own good.” “You and I are both scientists, ” laughed Tyler, “but you remember how we both thought that this surely was proof of some higher power too when the discovery was first publicised? Two birds with one stone! It keeps the majority of us merrily alive, while also ensuring that we would not run about unlocking the secrets of the universe until we were ready? ” There was no denying the contributions Donners had made to humankind. Tyler casually glanced around the room and out the window, and easily counted a dozen inventions which could not have been possible without the Donners. The hovercars, the bacterial foods with customizable tastes, implantable microchips for constant connection to the internet… even the drugs which commuted what would have been a death sentence for Valerie a decade ago to a mere ( if expensive ) annoyance. In a way, Tyler felt relief from having failed to qualify as a Donner. He had seen first-hand how some of the most emotionally-staunch people had been reduced to forlorn desolate souls once the Perogon-X2 was filtered out with the Masks. The degenerative process was universal – Donners would immediately benefit from heightened intelligence, but over time, they would latch onto and stubbornly nurse the perception that life was utterly… meaningless. Even if Donners were subsequently re-exposed to Perogon-X2, only 2 in 10 ever adapted back to normal life. The rest… preferred to simply put an end to it all. Roni’s voice snapped Tyler out of his reverie. “Tyler, remember how I begged you not to apply to be a Donner? ” “Yes, I remember.” “And you told me that you had no choice, because Valerie meant the world to you, and this was the least you could do as a parent for her? ” “Why are you bringing that up now? ” said Tyler with a flash of irritation. “I told you, I’ve been rejected. I can’t be a Donner anymore. We’ll just have to find another way.” Roni reached back into her handbag, and passed over a crisply-folded letter on embossed paper. Tyler began reading, and while he remained expressionless, Roni noted the bulging vein in the middle of his forehead, Tyler’s tell-tale indication of agitation. Roni wondered how much resistance Tyler was going to muster, but in her heart, she knew what she had to do. “I applied as well, Tyler, and they accepted me. They’ve already fitted my Mask, and I’ll be Donning it next Monday. We’ll have enough for Valerie after all.” -- - /r/rarelyfunny"

    bert_story = "I just want to tell you to go home. You will be fine. We're doing your next five minutes to reach the next building and feed on that mess that is the past you have made and you will lead a healthy life and that is something that I will teach you to have. Thanks for reading! ⁇ Have you ever tried r/WritingPrompts? More than ever you come up with a series of prompts that inspire you to write about the prompt, or the world you post. I don't do magic, but I write when I write about it. For example, to your friends of mine, I read a prompt that got a writing prompt and got asked to post it and my comment worked. No, I write about plants or science, and that answer is wrong. The ground is bigger than the sky, the elements in the universe are different, where you put you feet together, how you feel and what you taste, who you are, what you want, who you look like, etc etc etc etc etc etc. And it's not much of a *leoderie* and I can't say that it's a lovely thing, but I hope you like it, it's an enjoyable story. EDIT: A word word. ⁇"

    gpt2_story = "The entire environment has been ripped up. It was only a matter of time before we discovered a way to use gas masks to stop our body from moving. To carry the toxic gas around in the air, one person has carried a gas mask. Two or three people have carried similar gas masks but with different qualities. They were different weights so they blended well together. One has a hairline but the other one looks normal. With the gas mask, you wouldn't need to wear it to stay conscious. They fed you fresh air and a pleasant smell, and slept soundly. You are immune to the gas even after you lose your ability to breathe. Now, two of the most prominent people to be studied have been with the new gas mask. The leading scientist, a man named Jesus, created an entire gas mask to go around the body and eat it up. He was very successful in his latest experiment. But, because of the mask, he failed to demonstrate any indication of the presence of a mind. Jesus was released, the fourth drug to be tested on, and nearly a week later his only opponent, a man named James, entered the arena. The field wore on through it's rays of light. The scientists had a deadly weapon, that it was supposed to kill, while the people were paralyzed in agony. Even the scientist, who was faced with the most painful testing ever, had to admit he had no illusions. The camera man ran, literally screaming at Jesus, while the scientists examined him in horror. However, he thought better of it. When all of a sudden, a bright blinding light engulfed the scientist. After running for over half an hour, Jesus, in a fit of coughing up blood, grabbed the gun from the scientist, then ran away. Just as the gunshots stopped, he realised the truth. The man in the lab was the one who killed Jesus. In what was it's power, he had killed Jesus. And it was all thanks to the gas mask, who then used it to kill himself. The metal fed into the air by Jesus only cost him a week of life. A group of high schoolers are having a bad day at school. Write about the adventures that ensue. Jim rolled his eyes as he sat up on the back of the folding chair, a sore shoulder that only meant more mornings to him. For what seemed like the briefest of moments, he was,"

    gpt2_tag_story = "The passage from God to me is excruciating. I had lived in my body a long time since I was tested and myself deemed fit for the rest of life. I fought my own wars against my parents, my peers and my oppressors, but it wasn't enough. I still had to work hard to climb my way up. We have had all the servants on our planet given command of the instruments. The scientist named Roman had developed a device to send messages in there that can transmit a signal that is directly sent back at earth. It is an ancient technology, a useless trade secret. I have it on my collar, strapped in my pants and in the pocket of my black coat, but it will suffice. I have spent much of my life in this position. The scientists had attempted to communicate to our world the technology for the purpose of locating a source of death but our physical forms and technology were severely weakened by the concentration of it. We have held them hostage for nearly a century, learning their language and ideas. I had built a small device capable of bringing their technologies back to our planet and through it found out that they were experimenting on us. I came up with the plans to communicate with them, using how I had calculated the length of time we would have left at each communication. I had prepared for this, as I had, for hundreds of years. I was in no state to be around those sorts of things. The scientist had provided all of us with human technology. I had hoped that after more decades of training and experimenting, I would feel invincible and not just for a few more hours of human life, but at the same time be constantly tested and learning the new systems and procedures. The scientists had allowed me to be in charge, an everyday citizen of the planet. I had made it as far as I could from the cold wastes to the plains. Once I was alone I heard the opening doors of a nuclear reactor spewing radiation. I had only time to wonder how the world had changed. I didn't know what to do. I was just making preparations for another day when the door I had intended to open opened slammed shut. A loud noise pierced the silence. It must be a beacon, I thought to myself. In the distance I could hear"

    # PROMPT_TEMPLATE_1="Based on the following six attributes:\n1. Relevance (how well the story matches the prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following two stories by first providing an analysis of the two stories with respect to the rating criteria, and then assigning an integer score (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format:\n###Analysis###:\n###Story1 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n\n###Story2 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n"

    # PROMPT_TEMPLATE_1="Based on the following six attributes:\n1. Relevance (how well the story matches the prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following two stories by first providing an analysis, and then assigning an integer score (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format:\n###Analysis###:\n###Story1 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n\n###Story2 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n"

    PROMPT_TEMPLATE_1="Based on the following six attributes:\n1. Relevance (how well the story matches the prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following two stories by first providing an analysis, and then assigning an integer score (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format:\n\n###Analysis###:\n\n###Story1 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n\n###Story2 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n"

    PROMPT_TEMPLATE_2 = "Based on the following six attributes:\n1. Relevance (how well the story matches its prompt).\n2. Coherence (how much the story makes sense).\n3. Empathy (how well the reader can understand the character’s emotions).\n4. Surprise (how surprising the end of the story is).\n5. Engagement (how much the reader can engage with the story).\n6. Complexity (how elaborate the story is).\nEvaluate the following two stories by assigning an integer score (from 1 to 5) to each attribute. Higher score means better.\n\nThe initial prompt of story is: {}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format: \n###Story1 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n\n###Story2 Ratings###\n*Relevance*: \n*Coherence*: \n*Empathy*: \n*Surprise*: \n*Engagement*: \n*Complexity*: \n\n###Explanations###:"

    PROMPT_TEMPLATE_3 = "Evaluate the overall quality of the following two stories with respect to the given story prompt, by assigning an integer score (from 1 to 5) to each story. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format strictly:\n###Story1 Ratings###\n**Overall Quality w.r.t. Prompt**: \n\n###Story2 Ratings###\n**Overall Quality w.r.t. Prompt**: \n"

    PROMPT_TEMPLATE_4 = "Evaluate the overall quality of the following two stories with respect to the given story prompt, by assigning an integer score (from 1 to 5) to each story. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format:\n###Story1 Ratings###\n*Overall Quality w.r.t. Prompt*: \n\n###Story2 Ratings###\n*Overall Quality w.r.t. Prompt*: \n\n###Explanations###:"

    PROMPT_TEMPLATE_5 = "Evaluate the overall quality of the following two stories with respect to the given story prompt, by first providing an analysis, and then assigning an integer score (from 1 to 5) to each story. Higher score means better.\n\nThe initial prompt of story is:\n{}\n\nStory1:\n{}\n\nStory2:\n{}\n\nIn your response, please use the following format:\n###Analysis###:\n\n###Story1 Ratings###\n*Overall Quality w.r.t. Prompt*: \n\n###Story2 Ratings###\n*Overall Quality w.r.t. Prompt*: \n"

    prompt = PROMPT_TEMPLATE_3.format(premise, human_story, gpt2_story)
    # prompt = PROMPT_TEMPLATE_2.format(premise, gpt2_story, gpt2_tag_story)
    print(prompt)
    print("=====================================================")
    response = get_response('gemini-pro', prompt)
    # response = get_response('gpt-4-0125-preview', prompt)
    # response = get_response('gemini-pro', prompt)
    print(response)

    # s = "*Relevance*: "
    # print(extract_first_number(s))