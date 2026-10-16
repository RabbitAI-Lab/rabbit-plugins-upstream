# Query jobs

```sh
wemol-cli jobs query --channel "channel-name" --id 123
```

The default `summary` returns a job overview. Request `--show progress|failure|results` directly when needed; a preliminary summary is unnecessary. `progress` describes execution progress for a module or the modules in a workflow; `failure` expands failure information; `results` lists artifacts without downloading files. Workflow connections belong to the capability's `structure` view.

Find jobs by combining `--query "purpose or name"`, `--tag "tag"`, `--status succeeded`, `--since "YYYY-MM-DD"`, and `--until "YYYY-MM-DD"`. Multiple tags must all match. An ID is also a query condition and can be combined with other filters. Interpret timestamps as supplied by the platform.

At most five matching jobs are displayed by default; `--limit` controls the displayed count. `selection.matched`, `returned`, and `truncated` describe matching and display scope. The runtime handles platform list pagination; narrow larger result sets by date, tag, status, or text. Lists come from an index; `coverage` describes freshness and degraded reads. Current execution state is read live through a known ID or the needed detail view.

`failure` and `results` fetch details automatically: short content appears in `details.inline`; long content is stored in a local JSON file referenced by `details.file`. Read that file as needed; it preserves the same structure, observation time, and coverage. `results` is a manifest; retrieve artifact contents with `deliver`. Distinguish unknown states, failed reads, and incomplete coverage. A missing match does not prove submission failed. Decide whether and when to query again based on the user's goal.

When the user requests cancellation, use `wemol-cli jobs cancel --channel "channel-name" --id 123`. Platform acceptance of the cancellation request does not prove computation has stopped; describe the returned facts.

Status filters and displays use the same states; `pending` and `queued` are distinct. Failed module counts follow platform execution states. If a successful state carries error evidence, the response preserves both and marks the conflict. Complete task metadata and currently available artifact coverage describe different scopes; artifacts not yet published are not necessarily abnormally missing.
