# Cloudflare Temporary Preview Reference

## Limits

- Require Node.js 18+, a root `index.html`, regular files only, no symlinks, at most 1,000 files, and a generated Worker no larger than 2 MiB.
- This script embeds assets in the Worker; it does not use the Workers Static Assets API. Unclaimed temporary accounts expire after 60 minutes.

## Failure handling

- Invalid input, missing terms acceptance, or unavailable Claim path: stop locally; do not provision an account.
- API 429: wait and retry once. API 401/403: report the error; never alter credentials.
- Non-JSON API response: report its HTTP status.
- A fresh Live URL can briefly return 500; retry its public GET for up to 30 seconds before treating deployment as failed.

## Official documentation

- [Temporary Accounts](https://developers.cloudflare.com/workers/platform/claim-deployments/)
- [Multipart upload metadata](https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/)
- [Workers limits](https://developers.cloudflare.com/workers/platform/limits/)
