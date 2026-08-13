# MiMo compatibility protocols

Load this reference only when an existing client already requires OpenAI
Responses or Anthropic Messages. New MiMo integrations use Chat Completions
from the main skill.

## OpenAI Responses

Authenticate with `OPENAI_API_KEY`, set the base URL to
`https://runapi.ai/v1`, and call `client.responses.create` with a supported
exact model ID and text `input`. Verify `output_text`, terminal `usage`, and a
completed response. Streaming must include `response.completed` and `[DONE]`.

## Anthropic Messages

Set the Anthropic client base URL to `https://runapi.ai`, use the RunAPI key as
`api_key`, and call `client.messages.create` with a supported exact model ID,
`max_tokens`, and text messages. Verify final text, `stop_reason`, and `usage`;
a stream is complete only after `message_stop`.

Apply the same stop boundary as the primary recipe: one evidence-backed shape
correction, at most one safe pre-response transport retry, and no automatic
model or protocol change after a terminal failure.
