"""Tool for checking node health on RustChain."""

import json
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel

from langchain_community.tools.rustchain.base import RustChainBaseTool


class GetNodeHealthSchema(BaseModel):
    """Input schema for GetNodeHealth."""
    # No input required


class RustChainGetNodeHealth(RustChainBaseTool):
    """Tool for checking RustChain node health status."""

    name: str = "get_node_health"
    description: str = "Check the health status of the RustChain blockchain node."

    args_schema: Type[GetNodeHealthSchema] = GetNodeHealthSchema

    def _run(
        self,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Check node health."""
        result = self._make_request("/health")
        
        if "error" in result:
            return json.dumps({"error": result["error"]})
        
        return json.dumps(result, indent=2)