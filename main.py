import uuid
import datetime
import time

def log_event(conversation_id: str, step: str, message: str):
    """
    Logs an event with a unique conversation ID, timestamp, and step information.
    This simulates a structured logging mechanism for observability.
    """
    timestamp = datetime.datetime.now().isoformat()
    # Using a truncated conversation_id for readability in console output
    print(f"[{timestamp}] [CONV_ID:{conversation_id[:8]}] [STEP:{step}] {message}")

class SimpleAIAgent:
    """
    A simplified AI agent demonstrating how conversation IDs can be used
    to trace interactions across multiple internal steps.
    """
    def __init__(self, agent_name: str = "MyObservableAgent"):
        self.agent_name = agent_name
        log_event("SYSTEM", "INIT", f"{self.agent_name} initialized.")

    def _receive_query(self, conversation_id: str, query: str):
        """Simulates receiving a user query, logging with the conversation ID."""
        log_event(conversation_id, "RECEIVE_QUERY", f"User query received: '{query}'")
        time.sleep(0.1) # Simulate some processing time
        return f"Processed query for: '{query}'"

    def _process_with_tool(self, conversation_id: str, processed_query: str):
        """Simulates an internal tool call or service interaction, logging with the conversation ID."""
        tool_name = "KnowledgeBaseLookup"
        log_event(conversation_id, "TOOL_CALL", f"Calling tool '{tool_name}' with data: '{processed_query}'")
        time.sleep(0.2) # Simulate tool latency
        tool_result = f"Data from '{tool_name}' for '{processed_query}'"
        log_event(conversation_id, "TOOL_RESULT", f"Tool '{tool_name}' returned: '{tool_result}'")
        return tool_result

    def _generate_response(self, conversation_id: str, tool_data: str):
        """Simulates generating a final response, logging with the conversation ID."""
        log_event(conversation_id, "GENERATE_RESPONSE", f"Generating response using tool data: '{tool_data}'")
        time.sleep(0.1) # Simulate response generation
        final_response = f"Based on our analysis of '{tool_data}', here is your answer."
        log_event(conversation_id, "RESPONSE_SENT", f"Agent response: '{final_response}'")
        return final_response

    def simulate_user_interaction(self, user_query: str):
        """
        Orchestrates a full user interaction, ensuring all steps share the same
        conversation ID for end-to-end traceability, a core concept of observability.
        """
        conversation_id = str(uuid.uuid4()) # Generate a unique ID for this conversation
        log_event(conversation_id, "CONVERSATION_START", f"New interaction started for query: '{user_query}'")

        # Each step explicitly passes and uses the conversation_id for logging
        processed_query = self._receive_query(conversation_id, user_query)
        tool_data = self._process_with_tool(conversation_id, processed_query)
        final_response = self._generate_response(conversation_id, tool_data)

        log_event(conversation_id, "CONVERSATION_END", "Interaction completed.")
        return final_response

if __name__ == "__main__":
    agent = SimpleAIAgent()

    print("\n--- Simulating Conversation 1 ---")
    agent.simulate_user_interaction("What is the capital of France?")

    print("\n--- Simulating Conversation 2 ---")
    agent.simulate_user_interaction("Tell me about quantum computing.")

    print("\n--- Simulating Conversation 3 ---")
    agent.simulate_user_interaction("What's the weather like today?")

    print("\n--- End of Demonstrations ---")
