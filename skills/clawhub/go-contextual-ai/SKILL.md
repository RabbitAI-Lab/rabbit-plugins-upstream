---
name: go-contextual-ai
description: Unofficial Go client for the Contextual AI API, generated with oapi-codegen. `contextual.NewClientWithResponses(baseURL, opts...)` from `github.com/psyb0t/go-contextual-ai` gives a typed method for every endpoint in Contextual AI's OpenAPI spec (agents, agent queries, datastores, documents, generate, LMUnit, parse jobs, rerank, users), with request structs and decoded `JSON200`/`JSON422` response fields. Auth is a bearer API key added through a request editor. Use when Go code needs to call the Contextual AI API, or already imports go-contextual-ai.
homepage: https://github.com/psyb0t/go-contextual-ai
user-invocable: true
metadata:
  openclaw:
    emoji: "🔎"
    requires:
      bins:
        - go
      env:
        - CONTEXTUAL_API_KEY
permissions:
  filesystem: "Guides edits to the Go source of the current project. The library reads and writes no files."
  shell: "The Go toolchain (`go get`, `go build`, `go test`) to add and compile the dependency."
  network: "`go get` fetches the module from your Go module proxy. At runtime the client sends HTTPS requests only to the base URL you pass, normally https://api.contextual.ai/v1."
---

# go-contextual-ai

Typed Go client for the Contextual AI API. Package `contextual`, generated from the spec Contextual AI publishes for its SDKs.

For install details, the method naming scheme and the operation list, see [references/setup.md](references/setup.md).

## Security & safety

- Read the API key from an environment variable such as `CONTEXTUAL_API_KEY`. Never hardcode it, commit it, or log it, and never print request headers.
- Requests and their data go only to the base URL passed to `NewClientWithResponses`. Use `https://api.contextual.ai/v1` unless the user names another Contextual AI host.
- Delete, reset, user removal and ingestion calls change the user's account. Call them only when the user asked for that change, and only on agents, datastores and documents the task owns.

## When to use

- Go code needs to query a Contextual AI agent, manage agents or datastores, ingest or list documents, or call generate, rerank, parse or LMUnit.
- The project already imports `github.com/psyb0t/go-contextual-ai`.

## When NOT to use

- The code is not Go. Contextual AI ships official Python and Node SDKs.
- You need streamed query output as parsed events. The client has no server-sent events parser; leave `Stream` unset to get one JSON response.

## Usage

```go
import (
	"context"
	"fmt"
	"net/http"
	"os"

	"github.com/google/uuid"
	"github.com/psyb0t/go-contextual-ai"
)

auth := contextual.WithRequestEditorFn(func(_ context.Context, req *http.Request) error {
	req.Header.Set("Authorization", "Bearer "+os.Getenv("CONTEXTUAL_API_KEY"))

	return nil
})

client, err := contextual.NewClientWithResponses("https://api.contextual.ai/v1", auth)
if err != nil {
	return err
}

limit := 20

datastores, err := client.ListDatastoresDatastoresGetWithResponse(
	ctx,
	&contextual.ListDatastoresDatastoresGetParams{Limit: &limit},
)
if err != nil {
	return err // transport failure
}

if datastores.JSON200 == nil {
	return fmt.Errorf("list datastores: status %d: %s", datastores.StatusCode(), datastores.Body)
}

for _, ds := range datastores.JSON200.Datastores {
	fmt.Println(ds.Id, ds.Name)
}
```

Querying an agent:

```go
agentID, err := uuid.Parse(os.Getenv("CONTEXTUAL_AGENT_ID"))
if err != nil {
	return err
}

res, err := client.QueryAgentsAgentIdQueryPostWithResponse(
	ctx,
	agentID,
	&contextual.QueryAgentsAgentIdQueryPostParams{},
	contextual.QueryRequestV1{
		Messages: []contextual.MessageAndRole{
			{Role: contextual.SenderTypeUser, Content: "What is the refund policy?"},
		},
	},
)
if err != nil {
	return err
}

if res.JSON200 != nil && res.JSON200.Message != nil {
	fmt.Println(res.JSON200.Message.Content)
}
```

## Errors

- A non-nil `err` is a transport or decoding failure.
- An HTTP error status is not an `err`. Check `StatusCode()`: `JSON200` is set on success, `JSON422` (`*HTTPValidationError`, with `Detail`) on a validation error, and `Body` always holds the raw response.
