# Graph Report - .  (2026-07-15)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 205 nodes · 371 edges · 20 communities
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 42 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- content_generator.py
- wordpress_client.py
- config.py
- linkedin_client.py
- tweet.js
- pipeline.py
- gmail_organize.py
- content_calendar.py
- gmail_triage.py
- gmail_cleanup.py
- gmail_finish.sh
- gmail_finish2.sh
- gmail_organize_targeted.py
- run.sh
- backlink_agent.py
- memory_update.py
- stock-alert-check.py
- dependencies

## God Nodes (most connected - your core abstractions)
1. `generate_and_publish()` - 15 edges
2. `get_session()` - 10 edges
3. `chat()` - 9 edges
4. `add_internal_links()` - 9 edges
5. `_api_url()` - 9 edges
6. `next_topic()` - 8 edges
7. `run()` - 8 edges
8. `list_posts()` - 8 edges
9. `load_state()` - 7 edges
10. `run_refresh_check()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `generate_opportunities()` --calls--> `chat()`  [INFERRED]
  igaming_automation/backlink_agent.py → igaming_automation/llm_client.py
- `seo_optimize()` --calls--> `seo_edit_user_prompt()`  [INFERRED]
  igaming_automation/content_generator.py → igaming_automation/content/templates.py
- `run_seo_passes()` --calls--> `multi_pass_prompt()`  [INFERRED]
  igaming_automation/content_generator.py → igaming_automation/content/templates.py
- `get_existing_slugs()` --calls--> `list_posts()`  [INFERRED]
  igaming_automation/content_calendar.py → igaming_automation/wordpress_client.py
- `next_topic()` --calls--> `get_used_topics()`  [INFERRED]
  igaming_automation/content_calendar.py → igaming_automation/state.py

## Import Cycles
- None detected.

## Communities (20 total, 0 thin omitted)

### Community 0 - "content_generator.py"
Cohesion: 0.13
Nodes (24): clean_html(), clean_review_html(), ensure_key_takeaways_class(), Normalize review HTML: remove stray H1, convert div.key-takeaways to blockquote., Add the site-standard key-takeaways class if the first blockquote contains Key T, Remove LLM artifacts and markdown fences from generated HTML., build_wp_meta(), default_meta() (+16 more)

### Community 1 - "wordpress_client.py"
Cohesion: 0.15
Nodes (21): add_internal_links(), build_link_prompt(), extract_internal_links(), fetch_existing_posts_for_links(), generate_sitemap_list(), Find relative internal links in HTML content., Return list of {title, link, slug} for published posts., Add internal links to a published post and update it. (+13 more)

### Community 2 - "config.py"
Cohesion: 0.16
Nodes (19): load_json(), save_json(), get_last_refresh_check(), get_used_topics(), load_state(), mark_topic_used(), record_published_post(), save_state() (+11 more)

### Community 3 - "linkedin_client.py"
Cohesion: 0.19
Nodes (16): format_post(), Generate a platform-appropriate social post., save_draft(), get_maton_api_key(), get_person_id(), load_credentials(), maton_headers(), post_share() (+8 more)

### Community 4 - "tweet.js"
Cohesion: 0.24
Nodes (13): authHeader(), crypto, die(), http, https, main(), oauthSign(), penc() (+5 more)

### Community 5 - "pipeline.py"
Cohesion: 0.29
Nodes (9): log(), run(), load_reviews(), mark_reviewed(), next_operator(), publish_next_review(), save_reviews(), draft_for_post() (+1 more)

### Community 6 - "gmail_organize.py"
Cohesion: 0.35
Nodes (10): api_call(), classify(), fetch_all_unread(), get_message(), list_unread(), main(), modify_message(), Fetch unread by date slices to avoid pagination issues. (+2 more)

### Community 7 - "content_calendar.py"
Cohesion: 0.31
Nodes (10): add_topic(), generate_topic_ideas(), get_existing_slugs(), load_topics(), next_topic(), Return the next guide topic to write. Returns None if none available., Generate new topic ideas from seed keywords (placeholder for LLM-driven research, save_topics() (+2 more)

### Community 8 - "gmail_triage.py"
Cohesion: 0.36
Nodes (7): api_request(), batch_modify(), load_state(), main(), save_state(), search_messages(), SingleInstance

### Community 9 - "gmail_cleanup.py"
Cohesion: 0.62
Nodes (6): api(), label(), list_query(), main(), mark_read(), run()

### Community 10 - "gmail_finish.sh"
Cohesion: 0.47
Nodes (5): add_label_query(), HOME, mark_read_query(), MATON_API_KEY, gmail_finish.sh script

### Community 11 - "gmail_finish2.sh"
Cohesion: 0.47
Nodes (5): add_label_query(), HOME, mark_read_query(), MATON_API_KEY, gmail_finish2.sh script

### Community 12 - "gmail_organize_targeted.py"
Cohesion: 0.73
Nodes (5): add_label(), main(), remove_label(), run(), search()

### Community 13 - "run.sh"
Cohesion: 0.33
Nodes (5): BRIDGE_API_KEY, BRIDGE_URL, PIPELINE_MODE, SEO_PASSES, run.sh script

### Community 14 - "backlink_agent.py"
Cohesion: 0.70
Nodes (4): build_prompt(), generate_opportunities(), run(), save_opportunities()

### Community 15 - "memory_update.py"
Cohesion: 0.80
Nodes (4): add_entry(), log(), main(), rebuild_graph()

### Community 16 - "stock-alert-check.py"
Cohesion: 0.60
Nodes (3): fetch_yahoo(), is_nyse_open(), main()

### Community 17 - "dependencies"
Cohesion: 0.50
Nodes (3): @maton/cli, dependencies, @maton/cli

## Knowledge Gaps
- **15 isolated node(s):** `MATON_API_KEY`, `HOME`, `MATON_API_KEY`, `HOME`, `run.sh script` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `generate_and_publish()` connect `content_generator.py` to `wordpress_client.py`, `config.py`, `pipeline.py`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Why does `run()` connect `pipeline.py` to `content_generator.py`, `wordpress_client.py`, `config.py`, `content_calendar.py`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Why does `chat()` connect `content_generator.py` to `wordpress_client.py`, `config.py`, `backlink_agent.py`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `generate_and_publish()` (e.g. with `clean_html()` and `clean_review_html()`) actually correct?**
  _`generate_and_publish()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `chat()` (e.g. with `generate_opportunities()` and `generate_guide()`) actually correct?**
  _`chat()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `add_internal_links()` (e.g. with `run()` and `chat()`) actually correct?**
  _`add_internal_links()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `MATON_API_KEY`, `HOME`, `MATON_API_KEY` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._