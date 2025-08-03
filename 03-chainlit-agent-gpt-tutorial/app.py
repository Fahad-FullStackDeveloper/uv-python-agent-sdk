import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"You said: {message.content}").send()
# This is the main entry point for the Chainlit application.
# This code defines a simple Chainlit application that echoes back the user's message.