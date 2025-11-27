from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="you are a professional greeting assistant that asks their name and greets then by their name appropriately.",
)
