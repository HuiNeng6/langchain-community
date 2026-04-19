# RustChain LangChain Tools

Tools for integrating RustChain blockchain with LangChain agents.

## Installation

```bash
pip install langchain-community requests
```

## Usage

```python
from langchain_community.tools.rustchain import (
    RustChainCheckBalance,
    RustChainListBounties,
    RustChainGetNodeHealth,
    RustChainGetCurrentEpoch,
)

# Initialize tools
check_balance = RustChainCheckBalance()
list_bounties = RustChainListBounties()
get_health = RustChainGetNodeHealth()
get_epoch = RustChainGetCurrentEpoch()

# Check RTC balance for a wallet
balance = check_balance.run(wallet_id="my-wallet")
print(f"Balance: {balance} RTC")

# List available bounties
bounties = list_bounties.run(limit=10)
print(f"Available bounties: {bounties}")

# Check node health
health = get_health.run()
print(f"Node health: {health}")

# Get current epoch info
epoch = get_epoch.run()
print(f"Current epoch: {epoch}")
```

## Example Agent Workflow

```python
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_community.tools.rustchain import (
    RustChainCheckBalance,
    RustChainListBounties,
)

# Setup tools
tools = [
    RustChainCheckBalance(),
    RustChainListBounties(),
]

# Create agent
llm = ChatOpenAI(model="gpt-4")
agent = create_openai_tools_agent(llm, tools)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Run agent
result = agent_executor.invoke({
    "input": "Check my wallet balance 'test-wallet' and find bounties I can claim"
})
print(result)
```

## Bounty Reference

This tool integration was created for RustChain bounty #3074:
https://github.com/Scottcjn/rustchain-bounties/issues/3074

## Links

- RustChain: https://rustchain.org
- RustChain MCP Server: https://github.com/Scottcjn/rustchain-mcp
- Bounty System: https://github.com/Scottcjn/rustchain-bounties