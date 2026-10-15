# Submit jobs

Confirm capability suitability, the channel, and the user's intent to compute. Prepare a local JSON file using the same `capability` returned for the selected candidate (replace the example reference with an actual result):

```sh
wemol-cli jobs prepare --channel "channel-name" --capability "flow:456" --output "/absolute/path/job.json"
```

For modules, specify `--method` when needed; the template contains editable inputs for that method. Workflow templates contain only the minimal entry inputs by default. To adjust a node, add its configuration with repeatable `--node "node-reference-or-unique-name"`. `prepare` creates a new file and does not submit computation.

Edit the generated JSON according to the returned contract, preserving types and defaults. Enter text as JSON strings using file editing or JSON serialization rather than embedding scientific content in shell arguments. Relative file paths in `inputs` resolve from the JSON file's directory. Use `name` to describe the purpose and `tags` to aid retrieval; no separate registration is needed. Do not invent internal connections or fixed fields absent from the template.

```sh
wemol-cli jobs submit --file "/absolute/path/job.json"
```

This single call covers validation, user approval when required, upload, and platform acceptance. The original call remains pending during approval. If the host terminal tool returns a process session, use that tool to continue waiting for the original process. A waiting message is not a submission failure and is not a reason to resubmit.

A successful submission returns `platform_receipt: accepted` and a platform job ID. `job_status` separately describes the latest confirmed execution state; `unknown` means completion has not been observed. A submitted job can later fail or be cancelled while submission itself remains successful. `job_observed_at`, when present, timestamps that observation. Success never implies that artifacts have been downloaded.

`processing_time` provides the platform owner's historical module evidence: average and maximum seconds, sample count, observation time, and limitations. These are recent completed module Tasks, not an ETA for this Job: samples are not matched to its method, input size or parameters, and queue-time inclusion is unknown. Missing statistics and Flow total durations remain explicitly unknown, never zero.

For recent, consistently short module histories, the runtime may keep this original call pending briefly after acceptance and return an observed terminal state directly. This is bounded by the original call timeout; it does not require another submission or agent-managed polling. A completed success can be followed by result retrieval and analysis in the current turn. Otherwise, preserve the Job ID and arrange any result-dependent work using the host's own scheduling/resumption capability. If that capability is unavailable, explain the limitation instead of promising automatic analysis.

After confirmed acceptance, the end of this brief wait, an observation failure, or a graceful call interruption does not undo submission or cancel the Job. A transport disconnect that prevents receipt delivery may still leave acceptance unknown to the caller. On validation failure, correct the file using the specific feedback. Rejection, timeout, or interruption ends the call. If the response cannot establish whether the platform accepted the job, preserve that uncertainty and use a name or tag query when useful before deciding what to do next; avoid blindly duplicating computation. There is no internal work ID for the agent to resume.

Submitted jobs are visible in Bridge's Tracking page or the standalone TUI's Jobs page. While the local runtime is running, it checks their state. The receipt declares whether user notifications are available; standalone TUI currently has no system notifications. Current state and module progress are available through [Query jobs](jobs.md), using the channel and returned job ID. Notifications inform the user; they do not resume the agent. Scheduled queries or agent resumption depend on the agent host's own capabilities.

The receipt's `tracking` describes whether observation is active, paused, degraded, settled or unavailable. `automatic_agent_resume: false` means the runtime has not scheduled the external Agent to resume. User notifications and continuation of the user's requested analysis are separate responsibilities. Do not interpret tracking as a promise that the Agent will automatically finish the remaining work.
