#!/usr/bin/env python3
"""Social scheduling helper: draft posts for new content."""

from social.linkedin_client import publish_or_draft as linkedin_publish_or_draft
from social.twitter_client import publish_or_draft as twitter_publish_or_draft


def draft_for_post(post_id: int, title: str, url: str, dry_run: bool = True):
    """Create X and LinkedIn drafts for a published post."""
    results = {
        "twitter": twitter_publish_or_draft(post_id, title, url, dry_run=dry_run),
        "linkedin": linkedin_publish_or_draft(post_id, title, url, dry_run=dry_run),
    }
    return results
