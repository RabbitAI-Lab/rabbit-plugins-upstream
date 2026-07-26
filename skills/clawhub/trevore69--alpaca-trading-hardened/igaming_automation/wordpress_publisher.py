#!/usr/bin/env python3
"""Backward-compatible re-export of wordpress_client."""

from wordpress_client import (
    create_post,
    get_categories,
    get_session,
    get_tags,
    list_posts,
    update_post,
)

__all__ = [
    "create_post",
    "get_categories",
    "get_session",
    "get_tags",
    "list_posts",
    "update_post",
]
