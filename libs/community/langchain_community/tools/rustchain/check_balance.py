"""Tool for checking RTC balance on RustChain."""

from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field

from langchain_community.tools.rustchain.base import RustChainBaseTool


class CheckBalanceSchema(BaseModel):
    """Input schema for CheckBalance."""

    wallet_id: str = Field(
        ...,
        description="The wallet ID or miner ID to check balance for.",
    )


class RustChainCheckBalance(RustChainBaseTool):
    """Tool for checking RTC token balance on RustChain."""

    name: str = "check_balance"
    description: str = "Check the RTC token balance for a given wallet ID on the RustChain blockchain."

    args_schema: Type[CheckBalanceSchema] = CheckBalanceSchema

    def _run(
        self,
        wallet_id: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> float:
        """Check balance for a wallet."""
        result = self._make_request("/balance", params={"miner_id": wallet_id})
        
        if "error" in result:
            return 0.0
        
        # Extract balance from response
        balance = result.get("balance", 0.0)
        return float(balance)