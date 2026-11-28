# Daytona access policy

An access policy limits which endpoints Daytona connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/daytona#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Daytona: its 104 read-only endpoints, plus deny rules for the 3 write endpoints a read rule would otherwise match. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create daytona --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "api/api-keys"},
    {"method": "GET", "path": "api/api-keys/current"},
    {"method": "GET", "path": "api/api-keys/{id}"},
    {"method": "GET", "path": "api/audit/organizations/{id}"},
    {"method": "GET", "path": "api/audit/scenarios"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/a11y/tree"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/display/info"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/display/windows"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/mouse/position"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/process-status"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/process/{id}/errors"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/process/{id}/logs"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/process/{id}/status"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/recordings"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/recordings/{id}"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/recordings/{id}/download"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/screenshot"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/screenshot/compressed"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/screenshot/region"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/screenshot/region/compressed"},
    {"method": "GET", "path": "toolbox/{id}/computeruse/status"},
    {"method": "GET", "path": "api/config"},
    {"method": "GET", "path": "api/docker-registry"},
    {"method": "GET", "path": "api/docker-registry/{id}"},
    {"method": "GET", "path": "toolbox/{id}/files"},
    {"method": "POST", "path": "toolbox/{id}/files/bulk-download"},
    {"method": "GET", "path": "toolbox/{id}/files/download"},
    {"method": "GET", "path": "toolbox/{id}/files/find"},
    {"method": "GET", "path": "toolbox/{id}/files/info"},
    {"method": "GET", "path": "toolbox/{id}/files/search"},
    {"method": "GET", "path": "toolbox/{id}/git/branches"},
    {"method": "GET", "path": "toolbox/{id}/git/history"},
    {"method": "GET", "path": "toolbox/{id}/git/status"},
    {"method": "GET", "path": "api/health"},
    {"method": "GET", "path": "api/health/ready"},
    {"method": "GET", "path": "toolbox/{id}/user-home-dir"},
    {"method": "GET", "path": "toolbox/{id}/version"},
    {"method": "GET", "path": "toolbox/{id}/work-dir"},
    {"method": "GET", "path": "toolbox/{id}/process/interpreter/context"},
    {"method": "GET", "path": "toolbox/{id}/lsp/document-symbols"},
    {"method": "GET", "path": "toolbox/{id}/lsp/workspacesymbols"},
    {"method": "GET", "path": "api/organizations"},
    {"method": "GET", "path": "api/organizations/invitations"},
    {"method": "GET", "path": "api/organizations/invitations/count"},
    {"method": "GET", "path": "api/organizations/sandbox-telemetry/disabled-organization-ids"},
    {"method": "GET", "path": "api/organizations/{id}"},
    {"method": "GET", "path": "api/organizations/{id}/available-sandbox-classes"},
    {"method": "GET", "path": "api/organizations/{id}/gpu-capacity"},
    {"method": "GET", "path": "api/organizations/{id}/identity-providers"},
    {"method": "GET", "path": "api/organizations/{id}/identity-providers/workos-sso-connections"},
    {"method": "GET", "path": "api/organizations/{id}/identity-providers/{id}"},
    {"method": "GET", "path": "api/organizations/{id}/invitations"},
    {"method": "GET", "path": "api/organizations/{id}/roles"},
    {"method": "GET", "path": "api/organizations/{id}/usage"},
    {"method": "GET", "path": "api/organizations/{id}/users"},
    {"method": "GET", "path": "api/regions"},
    {"method": "GET", "path": "api/regions/{id}"},
    {"method": "GET", "path": "toolbox/{id}/port"},
    {"method": "GET", "path": "toolbox/{id}/port/{id}/in-use"},
    {"method": "GET", "path": "api/preview/{id}/access"},
    {"method": "GET", "path": "api/preview/{id}/preview-warning"},
    {"method": "GET", "path": "api/preview/{id}/public"},
    {"method": "GET", "path": "toolbox/{id}/process/pty"},
    {"method": "GET", "path": "toolbox/{id}/process/pty/{id}"},
    {"method": "GET", "path": "toolbox/{id}/process/session"},
    {"method": "GET", "path": "toolbox/{id}/process/session/entrypoint"},
    {"method": "GET", "path": "toolbox/{id}/process/session/entrypoint/logs"},
    {"method": "GET", "path": "toolbox/{id}/process/session/{id}"},
    {"method": "GET", "path": "toolbox/{id}/process/session/{id}/command/{id}"},
    {"method": "GET", "path": "toolbox/{id}/process/session/{id}/command/{id}/logs"},
    {"method": "GET", "path": "api/shared-regions"},
    {"method": "GET", "path": "api/runners"},
    {"method": "GET", "path": "api/runners/by-snapshot-ref"},
    {"method": "GET", "path": "api/runners/me/snapshots"},
    {"method": "GET", "path": "api/runners/{id}"},
    {"method": "GET", "path": "api/sandbox"},
    {"method": "GET", "path": "api/sandbox/ssh-access/validate"},
    {"method": "GET", "path": "api/sandbox/{id}"},
    {"method": "GET", "path": "api/sandbox/{id}/ancestors"},
    {"method": "GET", "path": "api/sandbox/{id}/build-logs"},
    {"method": "GET", "path": "api/sandbox/{id}/build-logs-url"},
    {"method": "GET", "path": "api/sandbox/{id}/forks"},
    {"method": "GET", "path": "api/sandbox/{id}/membership-operations/{id}"},
    {"method": "GET", "path": "api/sandbox/{id}/organization"},
    {"method": "GET", "path": "api/sandbox/{id}/parent"},
    {"method": "GET", "path": "api/sandbox/{id}/region-quota"},
    {"method": "GET", "path": "api/sandbox/{id}/telemetry/logs"},
    {"method": "GET", "path": "api/sandbox/{id}/telemetry/metrics"},
    {"method": "GET", "path": "api/sandbox/{id}/telemetry/traces"},
    {"method": "GET", "path": "api/sandbox/{id}/telemetry/traces/{id}"},
    {"method": "GET", "path": "api/sandbox/{id}/toolbox-proxy-url"},
    {"method": "GET", "path": "api/snapshots"},
    {"method": "GET", "path": "api/snapshots/{id}"},
    {"method": "GET", "path": "api/snapshots/{id}/build-logs"},
    {"method": "GET", "path": "api/snapshots/{id}/build-logs-url"},
    {"method": "GET", "path": "toolbox/{id}/system/metrics"},
    {"method": "GET", "path": "api/users/account-providers"},
    {"method": "GET", "path": "api/users/me"},
    {"method": "GET", "path": "api/users/me/pending-sso-links"},
    {"method": "GET", "path": "api/volumes"},
    {"method": "GET", "path": "api/volumes/by-name/{id}"},
    {"method": "GET", "path": "api/volumes/{id}"},
    {"method": "GET", "path": "api/warm-pools"},
    {"method": "GET", "path": "api/webhooks/organizations/{id}/initialization-status"}
  ],
  "deny": [
    {"method": "GET", "path": "api/docker-registry/registry-push-access"},
    {"method": "GET", "path": "api/runners/me"},
    {"method": "GET", "path": "api/sandbox/for-runner"}
  ]
}
```

## Endpoints

The Daytona endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | api/api-keys | read | api keys | List API keys: names, permissions and masked key values. |
| POST | api/api-keys | write | api keys | Create API key. |
| GET | api/api-keys/current | read | api keys | Get the connected API key’s name, permissions and masked value. |
| DELETE | api/api-keys/{id} | write | api keys | Delete API key. |
| GET | api/api-keys/{id} | read | api keys | Get an API key: its name, permissions and masked value. |
| DELETE | api/api-keys/{id}/{id} | write | api keys | Delete API key for user. |
| GET | api/audit/organizations/{id} | read | audit | Get audit logs for organization. |
| GET | api/audit/scenarios | read | audit | Get supported audit log scenarios. |
| POST | toolbox/{id}/computeruse/a11y/find | write | computer use | Find accessibility nodes. |
| POST | toolbox/{id}/computeruse/a11y/node/focus | write | computer use | Focus an accessibility node. |
| POST | toolbox/{id}/computeruse/a11y/node/invoke | write | computer use | Invoke an action on an accessibility node. |
| POST | toolbox/{id}/computeruse/a11y/node/value | write | computer use | Set the value of an accessibility node. |
| GET | toolbox/{id}/computeruse/a11y/tree | read | computer use | Get accessibility tree. |
| GET | toolbox/{id}/computeruse/display/info | read | computer use | Get display information. |
| GET | toolbox/{id}/computeruse/display/windows | read | computer use | Get windows information. |
| POST | toolbox/{id}/computeruse/keyboard/down | write | computer use | Press and hold a keyboard key. |
| POST | toolbox/{id}/computeruse/keyboard/hotkey | write | computer use | Press hotkey. |
| POST | toolbox/{id}/computeruse/keyboard/key | write | computer use | Press key. |
| POST | toolbox/{id}/computeruse/keyboard/type | write | computer use | Type text. |
| POST | toolbox/{id}/computeruse/keyboard/up | write | computer use | Release a held keyboard key. |
| POST | toolbox/{id}/computeruse/mouse/click | write | computer use | Click mouse button. |
| POST | toolbox/{id}/computeruse/mouse/down | write | computer use | Press mouse button. |
| POST | toolbox/{id}/computeruse/mouse/drag | write | computer use | Drag mouse. |
| POST | toolbox/{id}/computeruse/mouse/move | write | computer use | Move mouse cursor. |
| GET | toolbox/{id}/computeruse/mouse/position | read | computer use | Get mouse position. |
| POST | toolbox/{id}/computeruse/mouse/scroll | write | computer use | Scroll mouse wheel. |
| POST | toolbox/{id}/computeruse/mouse/up | write | computer use | Release mouse button. |
| GET | toolbox/{id}/computeruse/process-status | read | computer use | Get computer use process status. |
| GET | toolbox/{id}/computeruse/process/{id}/errors | read | computer use | Get process errors. |
| GET | toolbox/{id}/computeruse/process/{id}/logs | read | computer use | Get process logs. |
| POST | toolbox/{id}/computeruse/process/{id}/restart | write | computer use | Restart specific process. |
| GET | toolbox/{id}/computeruse/process/{id}/status | read | computer use | Get specific process status. |
| GET | toolbox/{id}/computeruse/recordings | read | computer use | List all recordings. |
| POST | toolbox/{id}/computeruse/recordings/start | write | computer use | Start a new recording. |
| POST | toolbox/{id}/computeruse/recordings/stop | write | computer use | Stop a recording. |
| DELETE | toolbox/{id}/computeruse/recordings/{id} | write | computer use | Delete a recording. |
| GET | toolbox/{id}/computeruse/recordings/{id} | read | computer use | Get recording details. |
| GET | toolbox/{id}/computeruse/recordings/{id}/download | read | computer use | Download a recording. |
| GET | toolbox/{id}/computeruse/screenshot | read | computer use | Take a screenshot. |
| GET | toolbox/{id}/computeruse/screenshot/compressed | read | computer use | Take a compressed screenshot. |
| GET | toolbox/{id}/computeruse/screenshot/region | read | computer use | Take a region screenshot. |
| GET | toolbox/{id}/computeruse/screenshot/region/compressed | read | computer use | Take a compressed region screenshot. |
| POST | toolbox/{id}/computeruse/start | write | computer use | Start computer use processes. |
| GET | toolbox/{id}/computeruse/status | read | computer use | Get computer use status. |
| POST | toolbox/{id}/computeruse/stop | write | computer use | Stop computer use processes. |
| GET | api/config | read | config | Get config. |
| GET | api/docker-registry | read | docker registry | List registries. |
| POST | api/docker-registry | write | docker registry | Create registry. |
| GET | api/docker-registry/registry-push-access | write | docker registry | Get temporary registry access for pushing snapshots. Kept out of read: returns registry credentials. |
| DELETE | api/docker-registry/{id} | write | docker registry | Delete registry. |
| GET | api/docker-registry/{id} | read | docker registry | Get registry. |
| PATCH | api/docker-registry/{id} | write | docker registry | Update registry. |
| DELETE | toolbox/{id}/files | write | file system | Delete a file or directory. |
| GET | toolbox/{id}/files | read | file system | List files and directories. |
| POST | toolbox/{id}/files/bulk-download | read | file system | Download multiple files. |
| POST | toolbox/{id}/files/bulk-upload | write | file system | Upload multiple files. |
| GET | toolbox/{id}/files/download | read | file system | Download a file. |
| GET | toolbox/{id}/files/find | read | file system | Find text in files. |
| POST | toolbox/{id}/files/folder | write | file system | Create a folder. |
| GET | toolbox/{id}/files/info | read | file system | Get file information. |
| POST | toolbox/{id}/files/move | write | file system | Move or rename file/directory. |
| POST | toolbox/{id}/files/permissions | write | file system | Set file permissions. |
| POST | toolbox/{id}/files/replace | write | file system | Replace text in files. |
| GET | toolbox/{id}/files/search | read | file system | Search files by pattern. |
| POST | toolbox/{id}/files/upload-v2 | write | file system | Upload a file. |
| POST | toolbox/{id}/git/add | write | git | Add files to Git staging. |
| DELETE | toolbox/{id}/git/branches | write | git | Delete a branch. |
| GET | toolbox/{id}/git/branches | read | git | List branches. |
| POST | toolbox/{id}/git/branches | write | git | Create a new branch. |
| POST | toolbox/{id}/git/checkout | write | git | Checkout branch or commit. |
| POST | toolbox/{id}/git/clone | write | git | Clone a Git repository. |
| POST | toolbox/{id}/git/commit | write | git | Commit changes. |
| GET | toolbox/{id}/git/config | write | git | Get a Git config value. Kept out of read: can include credentials in values or remote URLs. |
| POST | toolbox/{id}/git/config | write | git | Set a Git config value. |
| POST | toolbox/{id}/git/config/user | write | git | Configure Git user. |
| POST | toolbox/{id}/git/credentials | write | git | Authenticate Git. |
| GET | toolbox/{id}/git/history | read | git | Get commit history. |
| POST | toolbox/{id}/git/init | write | git | Initialize a Git repository. |
| POST | toolbox/{id}/git/pull | write | git | Pull changes from remote. |
| POST | toolbox/{id}/git/push | write | git | Push changes to remote. |
| GET | toolbox/{id}/git/remotes | write | git | List remotes. Kept out of read: can include credentials in values or remote URLs. |
| POST | toolbox/{id}/git/remotes | write | git | Add a remote. |
| POST | toolbox/{id}/git/reset | write | git | Reset repository. |
| POST | toolbox/{id}/git/restore | write | git | Restore files. |
| GET | toolbox/{id}/git/status | read | git | Get Git status. |
| GET | api/health | read | health | . |
| GET | api/health/ready | read | health | . |
| GET | toolbox/{id}/user-home-dir | read | info | Get user home directory. |
| GET | toolbox/{id}/version | read | info | Get version. |
| GET | toolbox/{id}/work-dir | read | info | Get working directory. |
| GET | toolbox/{id}/process/interpreter/context | read | interpreter | List all user-created interpreter contexts. |
| POST | toolbox/{id}/process/interpreter/context | write | interpreter | Create a new interpreter context. |
| DELETE | toolbox/{id}/process/interpreter/context/{id} | write | interpreter | Delete an interpreter context. |
| GET | toolbox/{id}/process/interpreter/execute | write | interpreter | Execute code in an interpreter context. Kept out of read: runs code in the sandbox. |
| GET | api/jobs | write | jobs | List jobs for the runner. Kept out of read: a runner endpoint that can claim jobs. |
| GET | api/jobs/poll | write | jobs | Long poll for jobs. Kept out of read: a runner endpoint that can claim jobs. |
| GET | api/jobs/{id} | write | jobs | Get job details. Kept out of read: a runner endpoint that can claim jobs. |
| POST | api/jobs/{id}/registry-mtls/{id} | write | jobs | Redeem registry mTLS credentials for an active job. |
| POST | api/jobs/{id}/status | write | jobs | Update job status. |
| POST | toolbox/{id}/lsp/completions | write | lsp | Get code completions. |
| POST | toolbox/{id}/lsp/did-close | write | lsp | Notify document closed. |
| POST | toolbox/{id}/lsp/did-open | write | lsp | Notify document opened. |
| GET | toolbox/{id}/lsp/document-symbols | read | lsp | Get document symbols. |
| POST | toolbox/{id}/lsp/start | write | lsp | Start LSP server. |
| POST | toolbox/{id}/lsp/stop | write | lsp | Stop LSP server. |
| GET | toolbox/{id}/lsp/workspacesymbols | read | lsp | Get workspace symbols. |
| GET | api/object-storage/push-access | write | object storage | Get temporary storage access for pushing objects. Kept out of read: returns storage credentials. |
| GET | api/organizations | read | organizations | List organizations. |
| POST | api/organizations | write | organizations | Create organization. |
| GET | api/organizations/invitations | read | organizations | List organization invitations for authenticated user. |
| GET | api/organizations/invitations/count | read | organizations | Get count of organization invitations for authenticated user. |
| POST | api/organizations/invitations/{id}/accept | write | organizations | Accept organization invitation. |
| POST | api/organizations/invitations/{id}/decline | write | organizations | Decline organization invitation. |
| GET | api/organizations/otel-config/by-sandbox-auth-token/{id} | write | organizations | Get organization OTEL config by sandbox auth token. Kept out of read: can include exporter credentials. |
| GET | api/organizations/sandbox-identity/by-sandbox-auth-token/{id} | write | organizations | Get sandbox identity by sandbox auth token. Kept out of read: takes a sandbox auth token. |
| GET | api/organizations/sandbox-telemetry/disabled-organization-ids | read | organizations | List organizations whose sandbox telemetry must not be stored. |
| DELETE | api/organizations/{id} | write | organizations | Delete organization. |
| GET | api/organizations/{id} | read | organizations | Get organization by ID. |
| GET | api/organizations/{id}/available-sandbox-classes | read | organizations | List available sandbox classes for organization. |
| PATCH | api/organizations/{id}/default-queue-timeout | write | organizations | Set organization default queue timeout. |
| PATCH | api/organizations/{id}/default-region | write | organizations | Set default region for organization. |
| PUT | api/organizations/{id}/experimental-config | write | organizations | Update experimental configuration. |
| GET | api/organizations/{id}/gpu-capacity | read | organizations | Get shared GPU capacity. |
| GET | api/organizations/{id}/identity-providers | read | organizations | List organization identity providers. Their OIDC client secrets are redacted. |
| POST | api/organizations/{id}/identity-providers | write | organizations | Create organization identity provider. |
| POST | api/organizations/{id}/identity-providers/test-connection | write | organizations | Test OIDC identity provider connection. |
| POST | api/organizations/{id}/identity-providers/workos-admin-portal-link | write | organizations | Generate a WorkOS Admin Portal link for configuring SSO or SCIM directory sync. |
| GET | api/organizations/{id}/identity-providers/workos-sso-connections | read | organizations | List the SSO connections configured for the organization in WorkOS. |
| DELETE | api/organizations/{id}/identity-providers/{id} | write | organizations | Delete organization identity provider. |
| GET | api/organizations/{id}/identity-providers/{id} | read | organizations | Get organization identity provider. Its OIDC client secret is redacted. |
| PATCH | api/organizations/{id}/identity-providers/{id} | write | organizations | Update organization identity provider. |
| GET | api/organizations/{id}/invitations | read | organizations | List pending organization invitations. |
| POST | api/organizations/{id}/invitations | write | organizations | Create organization invitation. |
| PUT | api/organizations/{id}/invitations/{id} | write | organizations | Update organization invitation. |
| POST | api/organizations/{id}/invitations/{id}/cancel | write | organizations | Cancel organization invitation. |
| POST | api/organizations/{id}/leave | write | organizations | Leave organization. |
| DELETE | api/organizations/{id}/otel-config | write | organizations | Delete organization OpenTelemetry configuration. |
| GET | api/organizations/{id}/otel-config | write | organizations | Get organization OTEL config by organization ID. Kept out of read: can include exporter credentials. |
| PUT | api/organizations/{id}/otel-config | write | organizations | Update organization OpenTelemetry configuration. |
| GET | api/organizations/{id}/roles | read | organizations | List organization roles. |
| POST | api/organizations/{id}/roles | write | organizations | Create organization role. |
| DELETE | api/organizations/{id}/roles/{id} | write | organizations | Delete organization role. |
| PUT | api/organizations/{id}/roles/{id} | write | organizations | Update organization role. |
| GET | api/organizations/{id}/usage | read | organizations | Get organization current usage overview. |
| GET | api/organizations/{id}/users | read | organizations | List organization members. |
| DELETE | api/organizations/{id}/users/{id} | write | organizations | Delete organization member. |
| POST | api/organizations/{id}/users/{id}/access | write | organizations | Update access for organization member. |
| GET | api/regions | read | organizations | List all available regions for the organization. |
| POST | api/regions | write | organizations | Create a new region. |
| DELETE | api/regions/{id} | write | organizations | Delete a region. |
| GET | api/regions/{id} | read | organizations | Get region by ID. |
| PATCH | api/regions/{id} | write | organizations | Update region configuration. |
| POST | api/regions/{id}/regenerate-proxy-api-key | write | organizations | Regenerate proxy API key for a region. |
| POST | api/regions/{id}/regenerate-snapshot-manager-credentials | write | organizations | Regenerate snapshot manager credentials for a region. |
| POST | api/regions/{id}/regenerate-ssh-gateway-api-key | write | organizations | Regenerate SSH gateway API key for a region. |
| GET | toolbox/{id}/port | read | port | Get active ports. |
| GET | toolbox/{id}/port/{id}/in-use | read | port | Check if port is in use. |
| GET | api/preview/{id}/access | read | preview | Check if user has access to the sandbox. |
| GET | api/preview/{id}/preview-warning | read | preview | Check if the preview warning page is enabled for the sandbox. |
| GET | api/preview/{id}/public | read | preview | Check if sandbox is public. |
| GET | api/preview/{id}/signing-key | write | preview | Get the signing key for a sandbox. Kept out of read: returns a signing key. |
| GET | api/preview/{id}/validate/{id} | write | preview | Check if sandbox auth token is valid. Kept out of read: takes a sandbox auth token. |
| GET | api/preview/{id}/{id}/sandbox-id | write | preview | Get sandbox ID from signed preview URL token. Kept out of read: takes a signed preview token. |
| POST | toolbox/{id}/process/code-run | write | process | Execute code. |
| POST | toolbox/{id}/process/execute | write | process | Execute a command. |
| GET | toolbox/{id}/process/pty | read | process | List all PTY sessions. |
| POST | toolbox/{id}/process/pty | write | process | Create a new PTY session. |
| DELETE | toolbox/{id}/process/pty/{id} | write | process | Delete a PTY session. |
| GET | toolbox/{id}/process/pty/{id} | read | process | Get PTY session information. |
| GET | toolbox/{id}/process/pty/{id}/connect | write | process | Connect to PTY session via WebSocket. Kept out of read: opens an interactive shell. |
| POST | toolbox/{id}/process/pty/{id}/resize | write | process | Resize a PTY session. |
| GET | toolbox/{id}/process/session | read | process | List all sessions. |
| POST | toolbox/{id}/process/session | write | process | Create a new session. |
| GET | toolbox/{id}/process/session/entrypoint | read | process | Get entrypoint session details. |
| GET | toolbox/{id}/process/session/entrypoint/logs | read | process | Get entrypoint logs. |
| DELETE | toolbox/{id}/process/session/{id} | write | process | Delete a session. |
| GET | toolbox/{id}/process/session/{id} | read | process | Get session details. |
| GET | toolbox/{id}/process/session/{id}/command/{id} | read | process | Get session command details. |
| POST | toolbox/{id}/process/session/{id}/command/{id}/input | write | process | Send input to command. |
| GET | toolbox/{id}/process/session/{id}/command/{id}/logs | read | process | Get session command logs. |
| POST | toolbox/{id}/process/session/{id}/exec | write | process | Execute command in session. |
| GET | api/shared-regions | read | regions | List all shared regions. |
| GET | api/runners | read | runners | List all runners. |
| POST | api/runners | write | runners | Create runner. |
| GET | api/runners/by-sandbox/{id} | write | runners | Get runner by sandbox ID. Kept out of read: returns a runner API key. |
| GET | api/runners/by-snapshot-ref | read | runners | Get runners by snapshot ref. |
| POST | api/runners/healthcheck | write | runners | Runner healthcheck. |
| GET | api/runners/me | write | runners | Get info for authenticated runner. Kept out of read: returns a runner API key. |
| GET | api/runners/me/snapshots | read | runners | Get snapshot refs for authenticated runner. |
| DELETE | api/runners/{id} | write | runners | Delete runner. |
| GET | api/runners/{id} | read | runners | Get runner by ID. |
| PATCH | api/runners/{id}/draining | write | runners | Update runner draining status. |
| GET | api/runners/{id}/full | write | runners | Get runner by ID. Kept out of read: returns a runner API key. |
| PATCH | api/runners/{id}/scheduling | write | runners | Update runner scheduling status. |
| GET | api/sandbox | read | sandbox | List sandboxes. |
| POST | api/sandbox | write | sandbox | Create a new sandbox. |
| GET | api/sandbox/for-runner | write | sandbox | Get sandboxes for the authenticated runner. Kept out of read: a runner endpoint that returns sandbox environment variables. |
| GET | api/sandbox/ssh-access/validate | read | sandbox | Validate SSH access for sandbox. |
| DELETE | api/sandbox/{id} | write | sandbox | Delete sandbox. |
| GET | api/sandbox/{id} | read | sandbox | Get sandbox details. The response includes the sandbox’s environment variables. |
| GET | api/sandbox/{id}/ancestors | read | sandbox | Get sandbox fork ancestor chain. |
| POST | api/sandbox/{id}/archive | write | sandbox | Archive sandbox. |
| POST | api/sandbox/{id}/autoarchive/{id} | write | sandbox | Set sandbox auto-archive interval. |
| POST | api/sandbox/{id}/autodelete/{id} | write | sandbox | Set sandbox auto-delete interval. |
| POST | api/sandbox/{id}/autopause/{id} | write | sandbox | Set sandbox auto-pause interval. |
| POST | api/sandbox/{id}/autostop/{id} | write | sandbox | Set sandbox auto-stop interval. |
| POST | api/sandbox/{id}/backup | write | sandbox | Create sandbox backup. |
| GET | api/sandbox/{id}/build-logs | read | sandbox | Get build logs. |
| GET | api/sandbox/{id}/build-logs-url | read | sandbox | Get build logs URL. |
| POST | api/sandbox/{id}/fork | write | sandbox | Fork a sandbox. |
| GET | api/sandbox/{id}/forks | read | sandbox | Get sandbox fork children. |
| PUT | api/sandbox/{id}/labels | write | sandbox | Replace sandbox labels. |
| POST | api/sandbox/{id}/last-activity | write | sandbox | Update sandbox last activity. |
| GET | api/sandbox/{id}/membership-operations/{id} | read | sandbox | Get a membership operation of a multi-node GPU sandbox. |
| POST | api/sandbox/{id}/network-settings | write | sandbox | Update sandbox network settings. |
| POST | api/sandbox/{id}/nodes | write | sandbox | Append nodes to a multi-node sandbox. |
| POST | api/sandbox/{id}/nodes/remove | write | sandbox | Remove the highest ranks from a multi-node sandbox. |
| POST | api/sandbox/{id}/nodes/{id}/replace | write | sandbox | Replace a failed multi-node sandbox rank. |
| GET | api/sandbox/{id}/organization | read | sandbox | Get organization by sandbox ID. |
| GET | api/sandbox/{id}/parent | read | sandbox | Get sandbox fork parent. |
| POST | api/sandbox/{id}/pause | write | sandbox | Pause sandbox. |
| GET | api/sandbox/{id}/ports/{id}/preview-url | write | sandbox | Get preview URL for a sandbox port. Kept out of read: returns a preview access token. |
| GET | api/sandbox/{id}/ports/{id}/signed-preview-url | write | sandbox | Get signed preview URL for a sandbox port. Kept out of read: returns a signed access URL. |
| POST | api/sandbox/{id}/ports/{id}/signed-preview-url/{id}/expire | write | sandbox | Expire signed preview URL for a sandbox port. |
| POST | api/sandbox/{id}/public/{id} | write | sandbox | Update public status. |
| POST | api/sandbox/{id}/recover | write | sandbox | Recover sandbox from error state. |
| GET | api/sandbox/{id}/region-quota | read | sandbox | Get region quota by sandbox ID. |
| POST | api/sandbox/{id}/resize | write | sandbox | Resize sandbox resources. |
| GET | api/sandbox/{id}/secrets | write | sandbox | Resolve sandbox secrets. Kept out of read: returns secret values. |
| PUT | api/sandbox/{id}/secrets | write | sandbox | Update sandbox secrets. |
| GET | api/sandbox/{id}/signing-key | write | sandbox | Get the signing key for a sandbox. Kept out of read: returns a signing key. |
| POST | api/sandbox/{id}/signing-key/rotate | write | sandbox | Rotate the signing key, invalidating all previously signed URLs. |
| POST | api/sandbox/{id}/snapshot | write | sandbox | Create a snapshot from a sandbox. |
| DELETE | api/sandbox/{id}/ssh-access | write | sandbox | Revoke SSH access for sandbox. |
| POST | api/sandbox/{id}/ssh-access | write | sandbox | Create SSH access for sandbox. |
| POST | api/sandbox/{id}/start | write | sandbox | Start or resume sandbox. |
| PUT | api/sandbox/{id}/state | write | sandbox | Update sandbox state. |
| POST | api/sandbox/{id}/stop | write | sandbox | Stop sandbox. |
| GET | api/sandbox/{id}/telemetry/logs | read | sandbox | Get sandbox logs. |
| GET | api/sandbox/{id}/telemetry/metrics | read | sandbox | Get sandbox metrics. |
| GET | api/sandbox/{id}/telemetry/traces | read | sandbox | Get sandbox traces. |
| GET | api/sandbox/{id}/telemetry/traces/{id} | read | sandbox | Get trace spans. |
| GET | api/sandbox/{id}/toolbox-proxy-url | read | sandbox | Get toolbox proxy URL for a sandbox. |
| POST | api/sandbox/{id}/ttl/{id} | write | sandbox | Set sandbox TTL. |
| GET | api/secret | write | secret | List secrets. Kept out of read: secrets may include values. |
| POST | api/secret | write | secret | Create secret. |
| GET | api/secret/paginated | write | secret | List secrets with pagination. Kept out of read: secrets may include values. |
| DELETE | api/secret/{id} | write | secret | Delete secret. |
| GET | api/secret/{id} | write | secret | Get secret. Kept out of read: secrets may include values. |
| PATCH | api/secret/{id} | write | secret | Update secret. |
| POST | toolbox/{id}/env | write | server | Update process environment. |
| POST | toolbox/{id}/init | write | server | Initialize toolbox server. |
| GET | api/snapshots | read | snapshots | List all snapshots. |
| POST | api/snapshots | write | snapshots | Create a new snapshot. |
| DELETE | api/snapshots/{id} | write | snapshots | Delete snapshot. |
| GET | api/snapshots/{id} | read | snapshots | Get snapshot by ID or name. |
| POST | api/snapshots/{id}/activate | write | snapshots | Activate a snapshot. |
| GET | api/snapshots/{id}/build-logs | read | snapshots | Get snapshot build logs. |
| GET | api/snapshots/{id}/build-logs-url | read | snapshots | Get snapshot build logs URL. |
| POST | api/snapshots/{id}/deactivate | write | snapshots | Deactivate a snapshot. |
| GET | toolbox/{id}/system/metrics | read | system | Get sandbox resource metrics. |
| GET | api/users/account-providers | read | users | Get account providers. |
| POST | api/users/linked-accounts | write | users | Link account (withdrawn). |
| GET | api/users/me | read | users | Get authenticated user. |
| POST | api/users/me/logins | write | users | Record a completed login. |
| GET | api/users/me/pending-sso-links | read | users | List pending SSO account links for the authenticated user. |
| DELETE | api/users/me/pending-sso-links/{id} | write | users | Dismiss a pending SSO account link. |
| POST | api/users/me/pending-sso-links/{id}/confirm | write | users | Confirm (link) a pending SSO account link. |
| POST | api/users/me/support-contacts | write | users | Record that a user refused by the email access gate reached for support. |
| POST | api/users/privacy-policies/accept | write | users | Accept the current privacy policies. |
| GET | api/volumes | read | volumes | List all volumes. |
| POST | api/volumes | write | volumes | Create a new volume. |
| GET | api/volumes/by-name/{id} | read | volumes | Get volume details by name. |
| DELETE | api/volumes/{id} | write | volumes | Delete volume. |
| GET | api/volumes/{id} | read | volumes | Get volume details. |
| GET | api/warm-pools | read | warm pools | List warm pools for the organization. |
| POST | api/warm-pools | write | warm pools | Create a warm pool. |
| DELETE | api/warm-pools/{id} | write | warm pools | Delete a warm pool. |
| PATCH | api/warm-pools/{id} | write | warm pools | Update a warm pool size. |
| POST | api/webhooks/organizations/{id}/app-portal-access | write | webhooks | Get Svix Consumer App Portal access for an organization. |
| GET | api/webhooks/organizations/{id}/initialization-status | read | webhooks | Get webhook initialization status for an organization. |
| POST | api/webhooks/organizations/{id}/initialize | write | webhooks | Initialize webhooks for an organization. |
| POST | api/webhooks/organizations/{id}/refresh-endpoints | write | webhooks | Refresh cached endpoint presence flag for an organization. |
