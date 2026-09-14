# Capability map and verified API contracts

## On-demand

Commands: `list_services`, `infer`, `get_request_status`, `get_upload_url`;
`theta.ondemand.listServices|infer|chat|status|inputPresignedUrls|pollUntilDone`.

Discovery base: `https://ondemand.thetaedgecloud.com/service/list?expand=template_id`.
Inspect all predictions, not just the default: image-to-image advertises separate
stylize/upscale/background-removal operations with different fields.
GLM uses `/infer_request/chat/completions`; job inference uses
`/infer_request/{service}?prediction=...&wait=...`. Request variant/webhook are
top-level; service input belongs under `input` for the job route.

The September 13 review found nine public aliases: `glm_5_3`, `glm_5_3_flash`,
`qwen3`, `blip`, `esrgan`, `whisper`, `image_to_image`,
`stable_diffusion_xl_turbo`, `llava`. This is a dated snapshot, NOT an allowlist
for future availability. FLUX/step_video/GPT-OSS and earlier Llamas were absent;
do not route a new image/video request to them without fresh discovery.

Normalized chat output keeps `output.message`, `output.tool_calls`, model,
finish reason, usage and reasoning separately. For tool continuation pass the
assistant message with `content:null, tool_calls:[...]`, then a tool message
with the matching `tool_call_id`. Never execute unvalidated model tool arguments.

## GPU and dedicated serving

- `theta.deployments.listVm`: raw VM resource/specification/price catalog.
- `theta.templates.listStandard`: category `prototyping`, `serving`, or `training`.
- `theta.templates.listCustom`: `projectId` or configured project.
- `theta.deployments.list|create|start|stop|delete|routeProbe|validateDisposable`.
- `theta.deployments.startByBaseId`: `baseId`, optional configured `projectId`;
  documented PUT `/deployments/base/{baseId}/start?project_id=...`.
  This is restart of a STOPPED node, not a proven atomic restart of a running one.
- `theta.billing.balance|balanceSnapshot`: org balance only. Numeric extraction
  does not by itself establish currency or a reliable spending delta.
- `theta.inference.models|chat|ready`: existing dedicated endpoints; select
  OpenAI `/v1/models` or Gradio `/config` readiness as appropriate.

Theta's August 27 announcement (updated September 11) adds hosted/community GPU
availability, regions, pricing, lifecycle, logs/events, usage breakdowns and
top-up history. These are NOT all implemented by the local wrapper. Public
`@thetalabs/on-demand-api-mcp@0.1.7` and its GitHub source still expose only four
on-demand tools. Do not claim it supports the expanded controller API surface.
For logs/events, detailed usage/top-up history or community availability:
obtain the current official tool/schema contract and inspect it before calling;
do not invent paths or label the VM type list a live capacity probe.

## RAG

`theta.ai.agent.create|get|update|list` and
`theta.ai.agent.document.create|update|get|list` accept project-scoped controller
credentials. Document create/update takes `file:{filename,content,contentType?,
encoding?}`; it does not read paths from disk. Existing settings payloads support
documented agent tool toggles, but there is no independently verified custom-tool
management wrapper. Do not claim deletion commands that are not registered.

## Video hosting and streams

`theta.video.list` takes `serviceAccountId`; also exposed:
`uploadCreate`, `create` (`payload`), `get` (`videoId`), `streamCreate`
(`payload`), `streamGet` (`streamId`), `ingestorList`, `ingestorSelect`
(`ingestorId`, `body`). These call `https://api.thetavideoapi.com` using Video
service-account credentials, not the on-demand token. Search, stream listing,
ingestor unselect and analytics are not registered; consult their API specs
before adding adapters. Video hosting is not on-demand generative video.

## AI Characters (new local adapter)

Official OpenAPI 1.0.0 base: `https://ai-chars-api.thetaedgecloud.com`.
Auth: separate per-game `THETA_CHARACTERS_API_KEY` Bearer token.
Registered `theta.characters.*` operations:
- `list|get|create|update|delete`: `gameId`, plus `characterId` for get/update/delete.
- `session.create`: payload matching SessionCreate.
- `session.get|session.delete`: `sessionId`.
- `session.list`: `gameId`.
- `session.context|session.message`: `sessionId`, `payload` matching the OpenAPI.
- `session.messages`: `sessionId`.

POST/PUT require an object `payload`. IDs are encoded, host is fixed, mutations
honor dry-run and are not retried automatically. Payload bodies remain spec-driven
pass-through; verify schemas when constructing them. No game creation, dashboard
session capture or game-key renewal is exposed. Runtime tests use fixtures;
live Characters tests require a configured game and approved test scope.

## Sources

- https://blog.thetatoken.org/ai-agents-can-now-deploy-edgecloud-gpus-themselves/
- https://blog.thetatoken.org/build-ai-characters-into-your-game-with-theta/
- https://github.com/thetatoken/on-demand-api-mcp
- https://github.com/thetatoken/theta-edge-cloud-ai-characters-public/blob/main/reference/ai-characters-openapi.json
- https://github.com/thetatoken/theta-edgecloud-chatbot-knowledge-example
- https://docs.thetatoken.org/docs/use-edgecloud-api-keys-to-manage-deployments

During the review the docs site blocked direct fetches (403). Previously imported
official deployment documentation was cross-checked with live read-only APIs;
the public GitHub specs, current blog and live service catalog were reachable.
