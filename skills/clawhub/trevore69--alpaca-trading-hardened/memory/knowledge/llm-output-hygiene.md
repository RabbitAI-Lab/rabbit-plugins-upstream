# LLM output hygiene (publishing)

LLM-generated articles leak artifacts. Before publishing to WordPress:

- Strip markdown code fences and stray backticks.
- Remove "Links added:"-style meta summaries.
- Check for trailing LLM summaries that are raw markdown, not HTML — strip explicitly.
- Key Takeaways box must be `<blockquote class="key-takeaways">`.
- No duplicate responsible-gambling disclaimers (site footer covers it).
