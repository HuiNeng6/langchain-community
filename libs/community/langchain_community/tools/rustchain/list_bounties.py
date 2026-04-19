"""Tool for listing bounties on RustChain."""

import json
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel, Field

from langchain_community.tools.rustchain.base import RustChainBaseTool


class ListBountiesSchema(BaseModel):
    """Input schema for ListBounties."""

    limit: int = Field(
        default=10,
        description="Maximum number of bounties to return.",
    )


class RustChainListBounties(RustChainBaseTool):
    """Tool for listing available bounties on RustChain."""

    name: str = "list_bounties"
    description: str = "List available bounties on the RustChain ecosystem that can be completed to earn RTC tokens."

    args_schema: Type[ListBountiesSchema] = ListBountiesSchema

    def _run(
        self,
        limit: int = 10,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """List bounties."""
        # Use bounty search endpoint from rustchain-mcp
        result = self._make_request("/bounties", params={"limit": limit})
        
        if "error" in result:
            return json.dumps({"error": result["error"]})
        
        # Format bounty list
        bounties = result.get("bounties", [])
        formatted_bounties = [
            {
                "title": b.get("title"),
                "reward": b.get("reward_rtc"),
                "url": b.get("url"),
                "status": b.get("status"),
            }
            for b in bounties[:limit]
        ]
        
        return json.dumps(formatted_bounties, indent=2)