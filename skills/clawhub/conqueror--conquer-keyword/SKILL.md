---
name: conquer-keyword
description: "Conquer a keyword: rewrite the connected WordPress site's best-matching page for it and propose the change as a reviewable diff with a before/after summary. Use to turn a target keyword into an actual page edit. Requires a connected Conqueror MCP server and a WordPress connection."
---

# Conquer a Keyword

## Goal

Take one target keyword and improve the connected WordPress site's best-matching page for it — better title, excerpt, structure, and content, matched to search intent — then propose the rewrite for human review. Proposing changes nothing on the site: the user reviews a diff in Conqueror and decides whether to apply it to the original post.

## Required inputs

- `projectId`
- The target keyword
- Optionally, a specific post/page to improve. Otherwise pick the best match.

If `projectId` is missing, use `list_projects` first. If the project has no WordPress connection, stop and tell the user to connect one in the project's settings page (Site URL + application password).

## Conqueror MCP tools

- `list_wordpress_posts`: find candidate posts (search by keyword). Includes drafts.
- `get_wordpress_post`: read the current title, excerpt, and body of the target post. The body is **raw editor content** — it may contain Gutenberg block comments (`<!-- wp:… -->`) and shortcodes.
- `get_serp_results`: see what currently ranks for the keyword.
- `get_keyword_metrics`: optional — attach volume/difficulty/intent to the keyword when useful context.
- `propose_wordpress_revision`: store the rewrite for review. Pass the post's `postId`; the current version is snapshotted so the user gets a diff and can roll back after applying.

You cannot apply, publish, or roll back a change. Those are the user's clicks in Conqueror.

## Workflow

1. **Find the target page.** `list_wordpress_posts` with the keyword as search. If one post is clearly the best match, use it; otherwise show the top candidates and ask the user to pick. Read it with `get_wordpress_post`.
2. **Understand the competition.** `get_serp_results` for the keyword; read 2-3 top-ranking pages to see the depth, structure, and subtopics that win. Note the dominant search intent (informational, commercial, transactional).
3. **Rewrite for the keyword.**
   - Title: include the keyword naturally, match intent, stay compelling.
   - Excerpt: a meta-description-quality summary (~150 chars) with the keyword.
   - Content: clear heading hierarchy (keyword in the lead), cover the gaps competitors expose, keep the site's voice, preserve real links and images. Improve what exists — do not pad with fluff or invent facts, prices, or statistics.
   - Preserve any block comments and shortcodes that were in the original, or the post loses its structure when the change is applied.
4. **Show before/after.** A compact comparison of title, excerpt, and structure plus the key content changes, with a one-line rationale per change.
5. **Propose it.** `propose_wordpress_revision` with the post's `postId`. Give the user the returned review link, and say plainly that nothing on the live site has changed yet.

## Output

- Before/after summary (title, excerpt, structure, key changes with rationale)
- The review link returned by `propose_wordpress_revision`
- One-line next step: review the diff and apply it to the original post
