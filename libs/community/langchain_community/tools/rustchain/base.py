"""Base class for RustChain tools."""

from __future__ import annotations

import requests
from typing import TYPE_CHECKING

from langchain_core.tools import BaseTool
from pydantic import Field


class RustChainBaseTool(BaseTool):
    """Base class for RustChain blockchain tools."""

    base_url: str = Field(default="https://rustchain.org")
    """The base URL for the RustChain API."""
    
    def _make_request(self, endpoint: str, params: dict = None) -> dict:
        """Make a request to the RustChain API."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.get(url, params=params, timeout=30, verify=False)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}