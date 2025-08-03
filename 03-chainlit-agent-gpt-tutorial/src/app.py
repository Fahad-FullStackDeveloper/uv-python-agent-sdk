import chainlit as cl

# Chat start par user se naam poochhna
@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Welcome to SmartBot!").send()

    # Ask name
    user_name = await cl.AskUserMessage(content="Aapka naam kya hai?").send()

    # Store user name for later use
    cl.user_session.set("name", user_name)

    # Show a greeting message with buttons
    actions = [
        cl.Action(name="help", value="madad", label="Madad Chahiye", payload={"type":"help"}),
        cl.Action(name="info", value="maloomat", label="Maloomat Chahiye", payload={"type":"info"}),
    ]

    await cl.Message(
        content=f"Shukriya, **{user_name}**! Ab aap kya karna chahtay hain?",
        actions=actions
    ).send()

# Jab user koi button click kare
@cl.action_callback
async def on_click(action):
    name = cl.user_session.get("name")
    if action.value == "madad":
        await cl.Message(content=f"**{name}**, madad ke liye hum yahan hain!").send()
    elif action.value == "maloomat":
        await cl.Message(content="Yeh lo aik choti image 😺").send()

        # Show image
        img = cl.Image(name="cat", path="src/assets/cat.jpg", display="inline")
        await cl.Message(content="Image below:", elements=[img]).send()

# Jab user kuch likhe ya file upload kare
@cl.on_message
async def handle_msg(message: cl.Message):
    if message.elements:
        for file in message.elements:
            await cl.Message(content=f"🗂 Aap ne file upload ki: `{file.name}`").send()
    else:
        await cl.Message(content=f"Aap ne likha: {message.content}").send()
