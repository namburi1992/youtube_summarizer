from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    # This is the default and can be omitted
    api_key="ollama",
)

def generate_summary_prompt(transcript_text, summary_length="brief", focus_points="main ideas", 
                            tone="neutral", audience="general public", additional_instructions="", 
                            output_format="paragraphs"):
    """
    Generate a summary prompt using the given template.
    
    :param transcript_text: The full transcript of the video.
    :param summary_length: Desired length of the summary (e.g., "brief," "detailed," "200 words").
    :param focus_points: Aspects of the video to emphasize in the summary (e.g., "main ideas," "key takeaways").
    :param tone: The tone of the summary (e.g., "formal," "informal," "neutral").
    :param audience: The target audience for the summary (e.g., "general public," "students").
    :param additional_instructions: Any special instructions for the summary.
    :param output_format: Preferred format for the summary (e.g., "paragraphs," "bullet points").
    
    :return: A formatted prompt string.
    """
    
    template = f"""
    Summarize the following transcript of a video. In not more than 250 words. 
    The summary should be concise and capture the key points discussed in the video. 
    
    **Transcript:**
    {transcript_text}

    **Summary Requirements:**
    1. Length: {summary_length}
    2. Focus on: {focus_points}
    3. Tone: {tone}
    4. Audience: {audience}
    5. Additional Instructions: {additional_instructions}

    Provide the summary in {output_format}.
    """ 
    
    return template.strip()

def summarize(transcript, **kwargs):
    try:
        chat_completion = client.chat.completions.create(messages=[
                                                            {
                                                                "role": "user",
                                                                "content": generate_summary_prompt(transcript),
                                                            }
                                                        ],
                                                        model="phi3:latest",
                                                        max_tokens = kwargs.get('max_tokens', 600),
                                                        temperature= kwargs.get('temperature', 0.8)
                                                    )
        
        response = chat_completion.choices[0].message.content
        return {"summary": response}
    except Exception as e:
        print(f"Error when requesting llms : {e}")
        return {}




if __name__ == "__main__":
    transcript = """
    foreign
[Music]
has a curious parrot called buddy buddy
has a great mimicking ability and a
sharp memory
buddy listens to all the conversations
in Peter's home and can mimic them very
accurately now when he hears feeling
hungry I would like to have some
for this case the probability of him
saying Biryani cherries or food is much
higher than the words such as bicycle or
book
but he doesn't understand the meaning of
Biryani or food or cherries the way
humans do all he is doing is using
statistical probability along with some
Randomness to predict the next word or
set of words be only based on the past
conversations he has listened to we can
call Buddy a stochastic parrot
stochastic Means A system that is
characterized by Randomness or
probability
a language model is somewhat like a
stochastic parrot their computer
programs that use a technology called
neural networks to predict the next set
of words for a sentence for a simple
explanation of a neural network please
watch this particular video
just like how birdies strain on Peter's
home conversations data set you can have
a language model that is trained on for
example all movie related articles from
Wikipedia and it will be able to predict
the next set of words for a movie
related sentence Gmail autocomplete is
one of the many applications that uses a
language model underneath
now that we have some understanding of a
language model let's understand what the
heck is a large language model
let's go back to our buddy example our
buddy got some Divine super power and
now he can listen to Peter's neighbors
conversations conversations that are
happening in schools and universities in
the town in fact not only in his town
but all the towns across the world
with this extra power and knowledge now
buddy can complete the next set of words
on a history subject
give your nutrition advice or even write
a poem like our powerful parrot body
large language models are trained on a
huge volume of data such as Wikipedia
articles Google news articles online
books and so on
if you look inside the llm you will find
a neural network containing trillions of
parameters that can capture more complex
patterns and nuances in a language chat
GPT is an application that uses llm
called gpt3 or gpt4 behind the scenes
examples of llms are Palm 2 by Google
and llama by meta
on top of statistical predictions llm
uses another approach called
reinforcement learning with human
feedback rlhf let's understand this once
again with Buddy one day Peter was
having a conversation with his cute
little two-year-old son
don't eat too much bananas else
hearing this Peter realized that buddy
has been listening to the conversations
from abusive parents in his town what he
said was the effect of that
Peter then starts skipping a close eye
on what buddy is saying for a same
question buddy can produce multiple
answers and all Peter has to do is tell
him which one is toxic and which one is
not
after this training buddy doesn't use
any toxic language
while training chat GPT open air used a
similar approach of human intervention
rlhf
open air used a huge Workforce of humans
to make chat GPT less toxic while llms
are very powerful they don't have any
subjective experience emotions or
Consciousness that we as humans have
llms work purely based on the data that
they have been trained on I hope you
like this short explanation which was
based on analogy obviously the technical
working of this thing is little
different than analogy but this should
give you a good intuition on this topic
if you like this video please share with
those who are curious about this topic
foreign
    """

    summary = summarize(transcript)
    print(summary)