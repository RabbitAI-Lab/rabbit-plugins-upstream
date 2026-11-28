# Google Meet access policy

An access policy limits which endpoints Google Meet connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-meet#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Google Meet: its 17 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create google-meet --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v2/conferenceRecords"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}"},
    {"method": "GET", "path": "v2/spaces/{id}/members"},
    {"method": "GET", "path": "v2/spaces/{id}/members/{id}"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/participants"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/participants/{id}"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/participants/{id}/participantSessions"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/participants/{id}/participantSessions/{id}"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/recordings"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/recordings/{id}"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/smartNotes"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/smartNotes/{id}"},
    {"method": "GET", "path": "v2/spaces/{id}"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/transcripts"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/transcripts/{id}"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/transcripts/{id}/entries"},
    {"method": "GET", "path": "v2/conferenceRecords/{id}/transcripts/{id}/entries/{id}"}
  ],
  "deny": []
}
```

## Endpoints

The Google Meet endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v2/conferenceRecords | read | conferenceRecords | Lists the conference records. |
| GET | v2/conferenceRecords/{id} | read | conferenceRecords | Gets a conference record by conference ID. |
| GET | v2/spaces/{id}/members | read | members | Lists members. |
| POST | v2/spaces/{id}/members | write | members | Creates a member. |
| GET | v2/spaces/{id}/members/{id} | read | members | Gets a member. |
| PATCH | v2/spaces/{id}/members/{id} | write | members | Updates a member. |
| DELETE | v2/spaces/{id}/members/{id} | write | members | Deletes the member who was previously assigned roles in the space. |
| POST | v2/spaces/{id}/members:batchUpdate | write | members | Updates members of one space within a batch. |
| GET | v2/conferenceRecords/{id}/participants | read | participants | Lists the participants in a conference record. |
| GET | v2/conferenceRecords/{id}/participants/{id} | read | participants | Gets a participant by participant ID. |
| GET | v2/conferenceRecords/{id}/participants/{id}/participantSessions | read | participants | Lists the participant sessions of a participant in a conference record. |
| GET | v2/conferenceRecords/{id}/participants/{id}/participantSessions/{id} | read | participants | Gets a participant session by participant session ID. |
| GET | v2/conferenceRecords/{id}/recordings | read | recordings | Lists the recording resources from the conference record. |
| GET | v2/conferenceRecords/{id}/recordings/{id} | read | recordings | Gets a recording by recording ID. |
| GET | v2/conferenceRecords/{id}/smartNotes | read | smartNotes | Lists the set of smart notes from the conference record. |
| GET | v2/conferenceRecords/{id}/smartNotes/{id} | read | smartNotes | Gets smart notes by smart note ID. |
| POST | v2/spaces | write | spaces | Creates a space. |
| GET | v2/spaces/{id} | read | spaces | Gets details about a meeting space. |
| PATCH | v2/spaces/{id} | write | spaces | Updates details about a meeting space. |
| POST | v2/spaces/{id}:endActiveConference | write | spaces | Ends an active conference (if there’s one). |
| GET | v2/conferenceRecords/{id}/transcripts | read | transcripts | Lists the set of transcripts from the conference record. |
| GET | v2/conferenceRecords/{id}/transcripts/{id} | read | transcripts | Gets a transcript by transcript ID. |
| GET | v2/conferenceRecords/{id}/transcripts/{id}/entries | read | transcripts | Lists the structured transcript entries per transcript. |
| GET | v2/conferenceRecords/{id}/transcripts/{id}/entries/{id} | read | transcripts | Gets a `TranscriptEntry` resource by entry ID. |
