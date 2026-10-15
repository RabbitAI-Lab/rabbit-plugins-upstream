# Retrieve artifacts

```sh
wemol-cli deliver --channel "channel-name" --job-id 123 --output "/absolute/path/results-parent"
```

When the task is to retrieve files and report computation state and retrieval completeness, call `deliver` directly. Its receipt includes `job_status`, `download_complete`, coverage, and the local directory. Query the job separately when node progress or failure reasons are needed. After obtaining the directory, select files to read and interpret according to the task.

Retrieval covers currently published artifacts; running, failed, and canceled jobs may also have files. `download_complete` describes only file retrieval for this call. Interpret it alongside `job_status` and coverage; it does not establish that the entire job has completed.

After interruption, keep existing files and repeat `deliver` with the same channel, job ID, and output parent directory. The runtime handles verification and available download resumption. Report absent artifacts, partial failures, or source file changes accurately; leftover files are not proof of success. Consult `deliver --help` to adjust time or size limits.
