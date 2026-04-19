"""Tool for getting current epoch info on RustChain."""

import json
from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from pydantic import BaseModel

from langchain_community.tools.rustchain.base import RustChainBaseTool


class GetCurrentEpochSchema(BaseModel):
    """Input schema for GetCurrentEpoch."""
    # No input required


class RustChainGetCurrentEpoch(RustChainBaseTool):
    """Tool for getting current epoch information on RustChain."""

    name: str = "get_current_epoch"
    description: str = "Get the current epoch information including epoch number, enrolled miners, and rewards on RustChain."

    args_schema: Type[GetCurrentEpochSchema] = GetCurrentEpochSchema

    def _run(
        self,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Get current epoch info."""
        result = self._make_request("/epoch")
        
        if "error" in result:
            return json.dumps({"error": result["error"]})
        
        return json.dumps(result, indent=2)