# Outlook access policy

An access policy limits which endpoints Outlook connections may call through Maton. Outlook doesn't offer a choice of OAuth scopes, so an access policy is the way to narrow a connection. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/outlook#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Outlook: its 237 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create outlook --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1.0/me"},
    {"method": "GET", "path": "v1.0/me/photo/**"},
    {"method": "GET", "path": "v1.0/me/photos/**"},
    {"method": "GET", "path": "v1.0/me/people/**"},
    {"method": "GET", "path": "v1.0/users/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/photo/**"},
    {"method": "GET", "path": "v1.0/users/{id}/photos/**"},
    {"method": "GET", "path": "v1.0/users/{id}/people/**"},
    {"method": "GET", "path": "v1.0/me/mailboxSettings/**"},
    {"method": "GET", "path": "v1.0/me/outlook/**"},
    {"method": "GET", "path": "v1.0/me/inferenceClassification/**"},
    {"method": "GET", "path": "v1.0/users/{id}/mailboxSettings/**"},
    {"method": "GET", "path": "v1.0/users/{id}/outlook/**"},
    {"method": "GET", "path": "v1.0/users/{id}/inferenceClassification/**"},
    {"method": "GET", "path": "v1.0/me/messages/**"},
    {"method": "POST", "path": "v1.0/me/getMailTips"},
    {"method": "POST", "path": "v1.0/me/translateExchangeIds"},
    {"method": "GET", "path": "v1.0/me/messages"},
    {"method": "GET", "path": "v1.0/me/messages/delta"},
    {"method": "GET", "path": "v1.0/me/messages/{id}"},
    {"method": "GET", "path": "v1.0/me/messages/{id}/$value"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages/delta"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages/{id}/$value"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages/delta"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/**"},
    {"method": "POST", "path": "v1.0/users/{id}/getMailTips"},
    {"method": "POST", "path": "v1.0/users/{id}/translateExchangeIds"},
    {"method": "GET", "path": "v1.0/users/{id}/messages"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/{id}/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages/{id}/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/$value"},
    {"method": "GET", "path": "v1.0/me/messages/{id}/attachments"},
    {"method": "GET", "path": "v1.0/me/messages/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/me/messages/{id}/attachments/{id}/$value"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages/{id}/attachments"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages/{id}/attachments/{id}/$value"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id}/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/{id}/attachments"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/{id}/attachments/{id}/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments/{id}/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id}/$value"},
    {"method": "GET", "path": "v1.0/me/messages/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messages/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/messages/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messages/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/**"},
    {"method": "GET", "path": "v1.0/me/mailFolders"},
    {"method": "GET", "path": "v1.0/me/mailFolders/delta"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/**"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messageRules"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/messageRules/{id}"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messageRules"},
    {"method": "GET", "path": "v1.0/me/mailFolders/{id}/childFolders/{id}/messageRules/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messageRules"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/messageRules/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messageRules"},
    {"method": "GET", "path": "v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messageRules/{id}"},
    {"method": "GET", "path": "v1.0/me/calendar/**"},
    {"method": "GET", "path": "v1.0/me/calendars/**"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/**"},
    {"method": "GET", "path": "v1.0/me/calendarView/**"},
    {"method": "GET", "path": "v1.0/me/calendar"},
    {"method": "GET", "path": "v1.0/me/calendars"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}"},
    {"method": "GET", "path": "v1.0/me/calendarGroups"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars"},
    {"method": "GET", "path": "v1.0/me/calendarView"},
    {"method": "GET", "path": "v1.0/me/calendar/calendarView"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/calendarView"},
    {"method": "POST", "path": "v1.0/me/calendar/getSchedule"},
    {"method": "POST", "path": "v1.0/me/calendars/{id}/getSchedule"},
    {"method": "POST", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/getSchedule"},
    {"method": "POST", "path": "v1.0/me/findMeetingTimes"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/**"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/**"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/**"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarView/**"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarView"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/calendarView"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/calendarView"},
    {"method": "POST", "path": "v1.0/users/{id}/calendar/getSchedule"},
    {"method": "POST", "path": "v1.0/users/{id}/calendars/{id}/getSchedule"},
    {"method": "POST", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/getSchedule"},
    {"method": "POST", "path": "v1.0/users/{id}/findMeetingTimes"},
    {"method": "GET", "path": "v1.0/me/calendar/calendarPermissions"},
    {"method": "GET", "path": "v1.0/me/calendar/calendarPermissions/{id}"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/calendarPermissions"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/calendarPermissions/{id}"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/calendarPermissions"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/calendarPermissions"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/calendarPermissions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/calendarPermissions"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/calendarPermissions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/calendarPermissions"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id}"},
    {"method": "GET", "path": "v1.0/me/events/**"},
    {"method": "GET", "path": "v1.0/me/events"},
    {"method": "GET", "path": "v1.0/me/events/delta"},
    {"method": "GET", "path": "v1.0/me/events/{id}"},
    {"method": "GET", "path": "v1.0/me/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/me/calendar/events"},
    {"method": "GET", "path": "v1.0/me/calendar/events/delta"},
    {"method": "GET", "path": "v1.0/me/calendar/events/{id}"},
    {"method": "GET", "path": "v1.0/me/calendar/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/events"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/events/delta"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/events/{id}"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/events"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/events/delta"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/users/{id}/events/**"},
    {"method": "GET", "path": "v1.0/users/{id}/events"},
    {"method": "GET", "path": "v1.0/users/{id}/events/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/events/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/events"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/events/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/events/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/events"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/events/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/events/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/instances"},
    {"method": "GET", "path": "v1.0/me/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/me/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/me/calendar/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/me/calendar/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/users/{id}/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/attachments"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/{id}"},
    {"method": "GET", "path": "v1.0/me/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/me/calendar/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/me/calendars/{id}/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendar/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendars/{id}/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id}"},
    {"method": "GET", "path": "v1.0/me/contacts/**"},
    {"method": "GET", "path": "v1.0/me/contacts"},
    {"method": "GET", "path": "v1.0/me/contacts/delta"},
    {"method": "GET", "path": "v1.0/me/contacts/{id}"},
    {"method": "GET", "path": "v1.0/me/contacts/{id}/photo"},
    {"method": "GET", "path": "v1.0/me/contacts/{id}/photo/$value"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/contacts"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/contacts/delta"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/contacts/{id}"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/contacts/{id}/photo"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/contacts/{id}/photo/$value"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/childFolders/{id}/contacts"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/delta"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/contacts/**"},
    {"method": "GET", "path": "v1.0/users/{id}/contacts"},
    {"method": "GET", "path": "v1.0/users/{id}/contacts/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/contacts/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/contacts/{id}/photo"},
    {"method": "GET", "path": "v1.0/users/{id}/contacts/{id}/photo/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/contacts"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/contacts/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/contacts/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/contacts/{id}/photo"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/contacts/{id}/photo/$value"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo/$value"},
    {"method": "GET", "path": "v1.0/me/contactFolders/**"},
    {"method": "GET", "path": "v1.0/me/contactFolders"},
    {"method": "GET", "path": "v1.0/me/contactFolders/delta"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}"},
    {"method": "GET", "path": "v1.0/me/contactFolders/{id}/childFolders"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/**"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/delta"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}"},
    {"method": "GET", "path": "v1.0/users/{id}/contactFolders/{id}/childFolders"},
    {"method": "POST", "path": "v1.0/search/query"},
    {"method": "GET", "path": "v1.0/subscriptions"},
    {"method": "GET", "path": "v1.0/subscriptions/{id}"}
  ],
  "deny": []
}
```

## Endpoints

The Outlook endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1.0/me | read | profile | Get the profile of the signed-in user. |
| PATCH | v1.0/me | write | profile | Update the profile of the signed-in user. |
| GET | `v1.0/me/photo/**` | read | profile | Read the profile photo of the signed-in user (metadata and $value content). |
| GET | `v1.0/me/photos/**` | read | profile | Read the available profile photo sizes of the signed-in user. |
| PUT | v1.0/me/photo/$value | write | profile | Replace the profile photo of the signed-in user. |
| PATCH | v1.0/me/photo/$value | write | profile | Replace the profile photo of the signed-in user. |
| DELETE | v1.0/me/photo/$value | write | profile | Delete the profile photo of the signed-in user. |
| GET | `v1.0/me/people/**` | read | profile | List or get people relevant to the signed-in user. |
| GET | v1.0/users/{id} | read | profile | Get the profile of a specified user. |
| PATCH | v1.0/users/{id} | write | profile | Update the profile of a specified user. |
| GET | `v1.0/users/{id}/photo/**` | read | profile | Read the profile photo of a specified user (metadata and $value content). |
| GET | `v1.0/users/{id}/photos/**` | read | profile | Read the available profile photo sizes of a specified user. |
| PUT | v1.0/users/{id}/photo/$value | write | profile | Replace the profile photo of a specified user. |
| PATCH | v1.0/users/{id}/photo/$value | write | profile | Replace the profile photo of a specified user. |
| DELETE | v1.0/users/{id}/photo/$value | write | profile | Delete the profile photo of a specified user. |
| GET | `v1.0/users/{id}/people/**` | read | profile | List or get people relevant to a specified user. |
| GET | `v1.0/me/mailboxSettings/**` | read | mailbox settings | Read mailbox settings of the signed-in user (automatic replies, time zone, working hours, locale). |
| PATCH | v1.0/me/mailboxSettings | write | mailbox settings | Update mailbox settings of the signed-in user, such as automatic replies. |
| GET | `v1.0/me/outlook/**` | read | mailbox settings | Read Outlook categories, supported languages and supported time zones of the signed-in user. |
| POST | v1.0/me/outlook/masterCategories | write | mailbox settings | Create an Outlook category for the signed-in user. |
| PATCH | v1.0/me/outlook/masterCategories/{id} | write | mailbox settings | Update an Outlook category of the signed-in user. |
| DELETE | v1.0/me/outlook/masterCategories/{id} | write | mailbox settings | Delete an Outlook category of the signed-in user. |
| GET | `v1.0/me/inferenceClassification/**` | read | mailbox settings | Read Focused Inbox classification and sender overrides of the signed-in user. |
| PATCH | v1.0/me/inferenceClassification | write | mailbox settings | Update the Focused Inbox classification of the signed-in user. |
| POST | v1.0/me/inferenceClassification/overrides | write | mailbox settings | Create a Focused Inbox sender override for the signed-in user. |
| PATCH | v1.0/me/inferenceClassification/overrides/{id} | write | mailbox settings | Update a Focused Inbox sender override of the signed-in user. |
| DELETE | v1.0/me/inferenceClassification/overrides/{id} | write | mailbox settings | Delete a Focused Inbox sender override of the signed-in user. |
| GET | `v1.0/users/{id}/mailboxSettings/**` | read | mailbox settings | Read mailbox settings of a specified user (automatic replies, time zone, working hours, locale). |
| PATCH | v1.0/users/{id}/mailboxSettings | write | mailbox settings | Update mailbox settings of a specified user, such as automatic replies. |
| GET | `v1.0/users/{id}/outlook/**` | read | mailbox settings | Read Outlook categories, supported languages and supported time zones of a specified user. |
| POST | v1.0/users/{id}/outlook/masterCategories | write | mailbox settings | Create an Outlook category for a specified user. |
| PATCH | v1.0/users/{id}/outlook/masterCategories/{id} | write | mailbox settings | Update an Outlook category of a specified user. |
| DELETE | v1.0/users/{id}/outlook/masterCategories/{id} | write | mailbox settings | Delete an Outlook category of a specified user. |
| GET | `v1.0/users/{id}/inferenceClassification/**` | read | mailbox settings | Read Focused Inbox classification and sender overrides of a specified user. |
| PATCH | v1.0/users/{id}/inferenceClassification | write | mailbox settings | Update the Focused Inbox classification of a specified user. |
| POST | v1.0/users/{id}/inferenceClassification/overrides | write | mailbox settings | Create a Focused Inbox sender override for a specified user. |
| PATCH | v1.0/users/{id}/inferenceClassification/overrides/{id} | write | mailbox settings | Update a Focused Inbox sender override of a specified user. |
| DELETE | v1.0/users/{id}/inferenceClassification/overrides/{id} | write | mailbox settings | Delete a Focused Inbox sender override of a specified user. |
| GET | `v1.0/me/messages/**` | read | messages | Read anything under the messages of the signed-in user: messages, MIME content, attachments, extensions, delta, $count. |
| POST | v1.0/me/sendMail | write | messages | Send a new email as the signed-in user. |
| POST | v1.0/me/getMailTips | read | messages | Look up mail tips (auto-reply text, mailbox-full, etc.) for recipients; POST only carries the query. |
| POST | v1.0/me/translateExchangeIds | read | messages | Convert Outlook item ids between formats for the signed-in user; POST only carries the ids. |
| GET | v1.0/me/messages | read | messages | List messages in the mailbox of the signed-in user. |
| GET | v1.0/me/messages/delta | read | messages | Track message changes in the mailbox of the signed-in user (delta query). |
| GET | v1.0/me/messages/{id} | read | messages | Get a message in the mailbox of the signed-in user. |
| GET | v1.0/me/messages/{id}/$value | read | messages | Get the MIME content of a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages | write | messages | Create a draft message in the mailbox of the signed-in user. |
| PATCH | v1.0/me/messages/{id} | write | messages | Update a message in the mailbox of the signed-in user (including marking it read or unread, flags and categories). |
| DELETE | v1.0/me/messages/{id} | write | messages | Delete a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/send | write | messages | Send an existing draft message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/reply | write | messages | Reply to the sender of a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/replyAll | write | messages | Reply to all recipients of a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/forward | write | messages | Forward a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/createReply | write | messages | Create a draft reply to a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/createReplyAll | write | messages | Create a draft reply-all to a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/createForward | write | messages | Create a draft forward of a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/move | write | messages | Move a message to another folder in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/copy | write | messages | Copy a message to another folder in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/permanentDelete | write | messages | Permanently delete a message in the mailbox of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messages | read | messages | List messages in a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messages/delta | read | messages | Track message changes in a mail folder of the signed-in user (delta query). |
| GET | v1.0/me/mailFolders/{id}/messages/{id} | read | messages | Get a message in a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messages/{id}/$value | read | messages | Get the MIME content of a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages | write | messages | Create a draft message in a mail folder of the signed-in user. |
| PATCH | v1.0/me/mailFolders/{id}/messages/{id} | write | messages | Update a message in a mail folder of the signed-in user (including marking it read or unread, flags and categories). |
| DELETE | v1.0/me/mailFolders/{id}/messages/{id} | write | messages | Delete a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/send | write | messages | Send an existing draft message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/reply | write | messages | Reply to the sender of a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/replyAll | write | messages | Reply to all recipients of a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/forward | write | messages | Forward a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/createReply | write | messages | Create a draft reply to a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/createReplyAll | write | messages | Create a draft reply-all to a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/createForward | write | messages | Create a draft forward of a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/move | write | messages | Move a message to another folder in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/copy | write | messages | Copy a message to another folder in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/permanentDelete | write | messages | Permanently delete a message in a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages | read | messages | List messages in a child mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/delta | read | messages | Track message changes in a child mail folder of the signed-in user (delta query). |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id} | read | messages | Get a message in a child mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/$value | read | messages | Get the MIME content of a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages | write | messages | Create a draft message in a child mail folder of the signed-in user. |
| PATCH | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id} | write | messages | Update a message in a child mail folder of the signed-in user (including marking it read or unread, flags and categories). |
| DELETE | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id} | write | messages | Delete a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/send | write | messages | Send an existing draft message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/reply | write | messages | Reply to the sender of a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/replyAll | write | messages | Reply to all recipients of a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/forward | write | messages | Forward a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/createReply | write | messages | Create a draft reply to a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/createReplyAll | write | messages | Create a draft reply-all to a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/createForward | write | messages | Create a draft forward of a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/move | write | messages | Move a message to another folder in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/copy | write | messages | Copy a message to another folder in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/permanentDelete | write | messages | Permanently delete a message in a child mail folder of the signed-in user. |
| GET | `v1.0/users/{id}/messages/**` | read | messages | Read anything under the messages of a specified user: messages, MIME content, attachments, extensions, delta, $count. |
| POST | v1.0/users/{id}/sendMail | write | messages | Send a new email as a specified user. |
| POST | v1.0/users/{id}/getMailTips | read | messages | Look up mail tips (auto-reply text, mailbox-full, etc.) for recipients; POST only carries the query. |
| POST | v1.0/users/{id}/translateExchangeIds | read | messages | Convert Outlook item ids between formats for a specified user; POST only carries the ids. |
| GET | v1.0/users/{id}/messages | read | messages | List messages in the mailbox of a specified user. |
| GET | v1.0/users/{id}/messages/delta | read | messages | Track message changes in the mailbox of a specified user (delta query). |
| GET | v1.0/users/{id}/messages/{id} | read | messages | Get a message in the mailbox of a specified user. |
| GET | v1.0/users/{id}/messages/{id}/$value | read | messages | Get the MIME content of a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages | write | messages | Create a draft message in the mailbox of a specified user. |
| PATCH | v1.0/users/{id}/messages/{id} | write | messages | Update a message in the mailbox of a specified user (including marking it read or unread, flags and categories). |
| DELETE | v1.0/users/{id}/messages/{id} | write | messages | Delete a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/send | write | messages | Send an existing draft message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/reply | write | messages | Reply to the sender of a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/replyAll | write | messages | Reply to all recipients of a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/forward | write | messages | Forward a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/createReply | write | messages | Create a draft reply to a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/createReplyAll | write | messages | Create a draft reply-all to a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/createForward | write | messages | Create a draft forward of a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/move | write | messages | Move a message to another folder in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/copy | write | messages | Copy a message to another folder in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/permanentDelete | write | messages | Permanently delete a message in the mailbox of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messages | read | messages | List messages in a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messages/delta | read | messages | Track message changes in a mail folder of a specified user (delta query). |
| GET | v1.0/users/{id}/mailFolders/{id}/messages/{id} | read | messages | Get a message in a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messages/{id}/$value | read | messages | Get the MIME content of a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages | write | messages | Create a draft message in a mail folder of a specified user. |
| PATCH | v1.0/users/{id}/mailFolders/{id}/messages/{id} | write | messages | Update a message in a mail folder of a specified user (including marking it read or unread, flags and categories). |
| DELETE | v1.0/users/{id}/mailFolders/{id}/messages/{id} | write | messages | Delete a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/send | write | messages | Send an existing draft message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/reply | write | messages | Reply to the sender of a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/replyAll | write | messages | Reply to all recipients of a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/forward | write | messages | Forward a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/createReply | write | messages | Create a draft reply to a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/createReplyAll | write | messages | Create a draft reply-all to a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/createForward | write | messages | Create a draft forward of a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/move | write | messages | Move a message to another folder in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/copy | write | messages | Copy a message to another folder in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/permanentDelete | write | messages | Permanently delete a message in a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages | read | messages | List messages in a child mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/delta | read | messages | Track message changes in a child mail folder of a specified user (delta query). |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id} | read | messages | Get a message in a child mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/$value | read | messages | Get the MIME content of a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages | write | messages | Create a draft message in a child mail folder of a specified user. |
| PATCH | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id} | write | messages | Update a message in a child mail folder of a specified user (including marking it read or unread, flags and categories). |
| DELETE | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id} | write | messages | Delete a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/send | write | messages | Send an existing draft message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/reply | write | messages | Reply to the sender of a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/replyAll | write | messages | Reply to all recipients of a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/forward | write | messages | Forward a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/createReply | write | messages | Create a draft reply to a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/createReplyAll | write | messages | Create a draft reply-all to a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/createForward | write | messages | Create a draft forward of a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/move | write | messages | Move a message to another folder in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/copy | write | messages | Copy a message to another folder in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/permanentDelete | write | messages | Permanently delete a message in a child mail folder of a specified user. |
| GET | v1.0/me/messages/{id}/attachments | read | message attachments | List attachments of a message in the mailbox of the signed-in user. |
| GET | v1.0/me/messages/{id}/attachments/{id} | read | message attachments | Get an attachment of a message in the mailbox of the signed-in user. |
| GET | v1.0/me/messages/{id}/attachments/{id}/$value | read | message attachments | Download the raw content of a message attachment in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/attachments | write | message attachments | Add an attachment to a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/attachments/createUploadSession | write | message attachments | Create an upload session to attach a large file to a message in the mailbox of the signed-in user. |
| DELETE | v1.0/me/messages/{id}/attachments/{id} | write | message attachments | Delete an attachment from a message in the mailbox of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messages/{id}/attachments | read | message attachments | List attachments of a message in a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messages/{id}/attachments/{id} | read | message attachments | Get an attachment of a message in a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messages/{id}/attachments/{id}/$value | read | message attachments | Download the raw content of a message attachment in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/attachments | write | message attachments | Add an attachment to a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/attachments/createUploadSession | write | message attachments | Create an upload session to attach a large file to a message in a mail folder of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id}/messages/{id}/attachments/{id} | write | message attachments | Delete an attachment from a message in a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments | read | message attachments | List attachments of a message in a child mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id} | read | message attachments | Get an attachment of a message in a child mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id}/$value | read | message attachments | Download the raw content of a message attachment in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments | write | message attachments | Add an attachment to a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/createUploadSession | write | message attachments | Create an upload session to attach a large file to a message in a child mail folder of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id} | write | message attachments | Delete an attachment from a message in a child mail folder of the signed-in user. |
| GET | v1.0/users/{id}/messages/{id}/attachments | read | message attachments | List attachments of a message in the mailbox of a specified user. |
| GET | v1.0/users/{id}/messages/{id}/attachments/{id} | read | message attachments | Get an attachment of a message in the mailbox of a specified user. |
| GET | v1.0/users/{id}/messages/{id}/attachments/{id}/$value | read | message attachments | Download the raw content of a message attachment in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/attachments | write | message attachments | Add an attachment to a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/attachments/createUploadSession | write | message attachments | Create an upload session to attach a large file to a message in the mailbox of a specified user. |
| DELETE | v1.0/users/{id}/messages/{id}/attachments/{id} | write | message attachments | Delete an attachment from a message in the mailbox of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments | read | message attachments | List attachments of a message in a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments/{id} | read | message attachments | Get an attachment of a message in a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments/{id}/$value | read | message attachments | Download the raw content of a message attachment in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments | write | message attachments | Add an attachment to a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments/createUploadSession | write | message attachments | Create an upload session to attach a large file to a message in a mail folder of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id}/messages/{id}/attachments/{id} | write | message attachments | Delete an attachment from a message in a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments | read | message attachments | List attachments of a message in a child mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id} | read | message attachments | Get an attachment of a message in a child mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id}/$value | read | message attachments | Download the raw content of a message attachment in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments | write | message attachments | Add an attachment to a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/createUploadSession | write | message attachments | Create an upload session to attach a large file to a message in a child mail folder of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/attachments/{id} | write | message attachments | Delete an attachment from a message in a child mail folder of a specified user. |
| GET | v1.0/me/messages/{id}/extensions/{id} | read | message extensions | Get an open extension of a message in the mailbox of the signed-in user. |
| POST | v1.0/me/messages/{id}/extensions | write | message extensions | Create an open extension on a message in the mailbox of the signed-in user. |
| PATCH | v1.0/me/messages/{id}/extensions/{id} | write | message extensions | Update an open extension of a message in the mailbox of the signed-in user. |
| DELETE | v1.0/me/messages/{id}/extensions/{id} | write | message extensions | Delete an open extension of a message in the mailbox of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messages/{id}/extensions/{id} | read | message extensions | Get an open extension of a message in a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messages/{id}/extensions | write | message extensions | Create an open extension on a message in a mail folder of the signed-in user. |
| PATCH | v1.0/me/mailFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Update an open extension of a message in a mail folder of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Delete an open extension of a message in a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id} | read | message extensions | Get an open extension of a message in a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions | write | message extensions | Create an open extension on a message in a child mail folder of the signed-in user. |
| PATCH | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Update an open extension of a message in a child mail folder of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Delete an open extension of a message in a child mail folder of the signed-in user. |
| GET | v1.0/users/{id}/messages/{id}/extensions/{id} | read | message extensions | Get an open extension of a message in the mailbox of a specified user. |
| POST | v1.0/users/{id}/messages/{id}/extensions | write | message extensions | Create an open extension on a message in the mailbox of a specified user. |
| PATCH | v1.0/users/{id}/messages/{id}/extensions/{id} | write | message extensions | Update an open extension of a message in the mailbox of a specified user. |
| DELETE | v1.0/users/{id}/messages/{id}/extensions/{id} | write | message extensions | Delete an open extension of a message in the mailbox of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messages/{id}/extensions/{id} | read | message extensions | Get an open extension of a message in a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messages/{id}/extensions | write | message extensions | Create an open extension on a message in a mail folder of a specified user. |
| PATCH | v1.0/users/{id}/mailFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Update an open extension of a message in a mail folder of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Delete an open extension of a message in a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id} | read | message extensions | Get an open extension of a message in a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions | write | message extensions | Create an open extension on a message in a child mail folder of a specified user. |
| PATCH | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Update an open extension of a message in a child mail folder of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messages/{id}/extensions/{id} | write | message extensions | Delete an open extension of a message in a child mail folder of a specified user. |
| GET | `v1.0/me/mailFolders/**` | read | mail folders | Read anything under the mail folders of the signed-in user: folders, child folders, their messages and attachments, rules, delta. |
| GET | v1.0/me/mailFolders | read | mail folders | List mail folders of the signed-in user. |
| GET | v1.0/me/mailFolders/delta | read | mail folders | Track mail folder changes of the signed-in user (delta query). |
| GET | v1.0/me/mailFolders/{id} | read | mail folders | Get a mail folder of the signed-in user (by id or well-known name such as Inbox). |
| GET | v1.0/me/mailFolders/{id}/childFolders | read | mail folders | List child folders of a mail folder of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id} | read | mail folders | Get a child folder of a mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders | write | mail folders | Create a mail folder for the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders | write | mail folders | Create a child folder in a mail folder of the signed-in user. |
| PATCH | v1.0/me/mailFolders/{id} | write | mail folders | Update a mail folder of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id} | write | mail folders | Delete a mail folder of the signed-in user. |
| PATCH | v1.0/me/mailFolders/{id}/childFolders/{id} | write | mail folders | Update a child mail folder of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id}/childFolders/{id} | write | mail folders | Delete a child mail folder of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/move | write | mail folders | Move a mail folder into another folder for the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/move | write | mail folders | Move a mail folder into another folder (child folder) for the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/copy | write | mail folders | Copy a mail folder into another folder for the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/copy | write | mail folders | Copy a mail folder into another folder (child folder) for the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/permanentDelete | write | mail folders | Permanently delete a mail folder for the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/permanentDelete | write | mail folders | Permanently delete a mail folder (child folder) for the signed-in user. |
| GET | `v1.0/users/{id}/mailFolders/**` | read | mail folders | Read anything under the mail folders of a specified user: folders, child folders, their messages and attachments, rules, delta. |
| GET | v1.0/users/{id}/mailFolders | read | mail folders | List mail folders of a specified user. |
| GET | v1.0/users/{id}/mailFolders/delta | read | mail folders | Track mail folder changes of a specified user (delta query). |
| GET | v1.0/users/{id}/mailFolders/{id} | read | mail folders | Get a mail folder of a specified user (by id or well-known name such as Inbox). |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders | read | mail folders | List child folders of a mail folder of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id} | read | mail folders | Get a child folder of a mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders | write | mail folders | Create a mail folder for a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders | write | mail folders | Create a child folder in a mail folder of a specified user. |
| PATCH | v1.0/users/{id}/mailFolders/{id} | write | mail folders | Update a mail folder of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id} | write | mail folders | Delete a mail folder of a specified user. |
| PATCH | v1.0/users/{id}/mailFolders/{id}/childFolders/{id} | write | mail folders | Update a child mail folder of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id}/childFolders/{id} | write | mail folders | Delete a child mail folder of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/move | write | mail folders | Move a mail folder into another folder for a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/move | write | mail folders | Move a mail folder into another folder (child folder) for a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/copy | write | mail folders | Copy a mail folder into another folder for a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/copy | write | mail folders | Copy a mail folder into another folder (child folder) for a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/permanentDelete | write | mail folders | Permanently delete a mail folder for a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/permanentDelete | write | mail folders | Permanently delete a mail folder (child folder) for a specified user. |
| GET | v1.0/me/mailFolders/{id}/messageRules | read | message rules | List inbox message rules of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/messageRules/{id} | read | message rules | Get an inbox message rule of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/messageRules | write | message rules | Create an inbox message rule for the signed-in user (rules can forward, move or delete mail). |
| PATCH | v1.0/me/mailFolders/{id}/messageRules/{id} | write | message rules | Update an inbox message rule of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id}/messageRules/{id} | write | message rules | Delete an inbox message rule of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messageRules | read | message rules | List inbox message rules of the signed-in user. |
| GET | v1.0/me/mailFolders/{id}/childFolders/{id}/messageRules/{id} | read | message rules | Get an inbox message rule of the signed-in user. |
| POST | v1.0/me/mailFolders/{id}/childFolders/{id}/messageRules | write | message rules | Create an inbox message rule for the signed-in user (rules can forward, move or delete mail). |
| PATCH | v1.0/me/mailFolders/{id}/childFolders/{id}/messageRules/{id} | write | message rules | Update an inbox message rule of the signed-in user. |
| DELETE | v1.0/me/mailFolders/{id}/childFolders/{id}/messageRules/{id} | write | message rules | Delete an inbox message rule of the signed-in user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messageRules | read | message rules | List inbox message rules of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/messageRules/{id} | read | message rules | Get an inbox message rule of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/messageRules | write | message rules | Create an inbox message rule for a specified user (rules can forward, move or delete mail). |
| PATCH | v1.0/users/{id}/mailFolders/{id}/messageRules/{id} | write | message rules | Update an inbox message rule of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id}/messageRules/{id} | write | message rules | Delete an inbox message rule of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messageRules | read | message rules | List inbox message rules of a specified user. |
| GET | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messageRules/{id} | read | message rules | Get an inbox message rule of a specified user. |
| POST | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messageRules | write | message rules | Create an inbox message rule for a specified user (rules can forward, move or delete mail). |
| PATCH | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messageRules/{id} | write | message rules | Update an inbox message rule of a specified user. |
| DELETE | v1.0/users/{id}/mailFolders/{id}/childFolders/{id}/messageRules/{id} | write | message rules | Delete an inbox message rule of a specified user. |
| GET | `v1.0/me/calendar/**` | read | calendars | Read anything under the default calendar of the signed-in user: events, calendarView, permissions, instances, delta. |
| GET | `v1.0/me/calendars/**` | read | calendars | Read anything under the calendars of the signed-in user: calendars, events, calendarView, permissions, delta. |
| GET | `v1.0/me/calendarGroups/**` | read | calendars | Read anything under the calendar groups of the signed-in user: groups, calendars and their events. |
| GET | `v1.0/me/calendarView/**` | read | calendars | List events of the signed-in user in a time range (occurrences expanded), including delta. |
| GET | v1.0/me/calendar | read | calendars | Get the default calendar of the signed-in user. |
| GET | v1.0/me/calendars | read | calendars | List calendars of the signed-in user. |
| GET | v1.0/me/calendars/{id} | read | calendars | Get a calendar of the signed-in user. |
| GET | v1.0/me/calendarGroups | read | calendars | List calendar groups of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id} | read | calendars | Get a calendar group of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars | read | calendars | List calendars in a calendar group of the signed-in user. |
| GET | v1.0/me/calendarView | read | calendars | List events of the signed-in user between startDateTime and endDateTime. |
| GET | v1.0/me/calendar/calendarView | read | calendars | List events in the default calendar of the signed-in user within a time range. |
| GET | v1.0/me/calendars/{id}/calendarView | read | calendars | List events in a calendar of the signed-in user within a time range. |
| POST | v1.0/me/calendar/getSchedule | read | calendars | Get free/busy availability for users and resources; POST only carries the query. |
| POST | v1.0/me/calendars/{id}/getSchedule | read | calendars | Get free/busy availability for users and resources; POST only carries the query. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/getSchedule | read | calendars | Get free/busy availability for users and resources; POST only carries the query. |
| POST | v1.0/me/findMeetingTimes | read | calendars | Suggest meeting times from attendee availability for the signed-in user; nothing is created. |
| POST | v1.0/me/calendars | write | calendars | Create a calendar for the signed-in user. |
| PATCH | v1.0/me/calendar | write | calendars | Update the default calendar of the signed-in user. |
| PATCH | v1.0/me/calendars/{id} | write | calendars | Update a calendar of the signed-in user. |
| DELETE | v1.0/me/calendars/{id} | write | calendars | Delete a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/permanentDelete | write | calendars | Permanently delete a calendar of the signed-in user. |
| POST | v1.0/me/calendarGroups | write | calendars | Create a calendar group for the signed-in user. |
| PATCH | v1.0/me/calendarGroups/{id} | write | calendars | Update a calendar group of the signed-in user. |
| DELETE | v1.0/me/calendarGroups/{id} | write | calendars | Delete a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars | write | calendars | Create a calendar in a calendar group of the signed-in user. |
| PATCH | v1.0/me/calendarGroups/{id}/calendars/{id} | write | calendars | Update a calendar in a calendar group of the signed-in user. |
| DELETE | v1.0/me/calendarGroups/{id}/calendars/{id} | write | calendars | Delete a calendar in a calendar group of the signed-in user. |
| GET | `v1.0/users/{id}/calendar/**` | read | calendars | Read anything under the default calendar of a specified user: events, calendarView, permissions, instances, delta. |
| GET | `v1.0/users/{id}/calendars/**` | read | calendars | Read anything under the calendars of a specified user: calendars, events, calendarView, permissions, delta. |
| GET | `v1.0/users/{id}/calendarGroups/**` | read | calendars | Read anything under the calendar groups of a specified user: groups, calendars and their events. |
| GET | `v1.0/users/{id}/calendarView/**` | read | calendars | List events of a specified user in a time range (occurrences expanded), including delta. |
| GET | v1.0/users/{id}/calendar | read | calendars | Get the default calendar of a specified user. |
| GET | v1.0/users/{id}/calendars | read | calendars | List calendars of a specified user. |
| GET | v1.0/users/{id}/calendars/{id} | read | calendars | Get a calendar of a specified user. |
| GET | v1.0/users/{id}/calendarGroups | read | calendars | List calendar groups of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id} | read | calendars | Get a calendar group of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars | read | calendars | List calendars in a calendar group of a specified user. |
| GET | v1.0/users/{id}/calendarView | read | calendars | List events of a specified user between startDateTime and endDateTime. |
| GET | v1.0/users/{id}/calendar/calendarView | read | calendars | List events in the default calendar of a specified user within a time range. |
| GET | v1.0/users/{id}/calendars/{id}/calendarView | read | calendars | List events in a calendar of a specified user within a time range. |
| POST | v1.0/users/{id}/calendar/getSchedule | read | calendars | Get free/busy availability for users and resources; POST only carries the query. |
| POST | v1.0/users/{id}/calendars/{id}/getSchedule | read | calendars | Get free/busy availability for users and resources; POST only carries the query. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/getSchedule | read | calendars | Get free/busy availability for users and resources; POST only carries the query. |
| POST | v1.0/users/{id}/findMeetingTimes | read | calendars | Suggest meeting times from attendee availability for a specified user; nothing is created. |
| POST | v1.0/users/{id}/calendars | write | calendars | Create a calendar for a specified user. |
| PATCH | v1.0/users/{id}/calendar | write | calendars | Update the default calendar of a specified user. |
| PATCH | v1.0/users/{id}/calendars/{id} | write | calendars | Update a calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendars/{id} | write | calendars | Delete a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/permanentDelete | write | calendars | Permanently delete a calendar of a specified user. |
| POST | v1.0/users/{id}/calendarGroups | write | calendars | Create a calendar group for a specified user. |
| PATCH | v1.0/users/{id}/calendarGroups/{id} | write | calendars | Update a calendar group of a specified user. |
| DELETE | v1.0/users/{id}/calendarGroups/{id} | write | calendars | Delete a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars | write | calendars | Create a calendar in a calendar group of a specified user. |
| PATCH | v1.0/users/{id}/calendarGroups/{id}/calendars/{id} | write | calendars | Update a calendar in a calendar group of a specified user. |
| DELETE | v1.0/users/{id}/calendarGroups/{id}/calendars/{id} | write | calendars | Delete a calendar in a calendar group of a specified user. |
| GET | v1.0/me/calendar/calendarPermissions | read | calendar permissions | List who a calendar of the signed-in user is shared with. |
| GET | v1.0/me/calendar/calendarPermissions/{id} | read | calendar permissions | Get a sharing permission of a calendar of the signed-in user. |
| POST | v1.0/me/calendar/calendarPermissions | write | calendar permissions | Share a calendar of the signed-in user with a user or delegate. |
| PATCH | v1.0/me/calendar/calendarPermissions/{id} | write | calendar permissions | Change a sharing permission on a calendar of the signed-in user. |
| DELETE | v1.0/me/calendar/calendarPermissions/{id} | write | calendar permissions | Remove a sharing permission from a calendar of the signed-in user. |
| GET | v1.0/me/calendars/{id}/calendarPermissions | read | calendar permissions | List who a calendar of the signed-in user is shared with. |
| GET | v1.0/me/calendars/{id}/calendarPermissions/{id} | read | calendar permissions | Get a sharing permission of a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/calendarPermissions | write | calendar permissions | Share a calendar of the signed-in user with a user or delegate. |
| PATCH | v1.0/me/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Change a sharing permission on a calendar of the signed-in user. |
| DELETE | v1.0/me/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Remove a sharing permission from a calendar of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/calendarPermissions | read | calendar permissions | List who a calendar of the signed-in user is shared with. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id} | read | calendar permissions | Get a sharing permission of a calendar of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/calendarPermissions | write | calendar permissions | Share a calendar of the signed-in user with a user or delegate. |
| PATCH | v1.0/me/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Change a sharing permission on a calendar of the signed-in user. |
| DELETE | v1.0/me/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Remove a sharing permission from a calendar of the signed-in user. |
| GET | v1.0/users/{id}/calendar/calendarPermissions | read | calendar permissions | List who a calendar of a specified user is shared with. |
| GET | v1.0/users/{id}/calendar/calendarPermissions/{id} | read | calendar permissions | Get a sharing permission of a calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/calendarPermissions | write | calendar permissions | Share a calendar of a specified user with a user or delegate. |
| PATCH | v1.0/users/{id}/calendar/calendarPermissions/{id} | write | calendar permissions | Change a sharing permission on a calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendar/calendarPermissions/{id} | write | calendar permissions | Remove a sharing permission from a calendar of a specified user. |
| GET | v1.0/users/{id}/calendars/{id}/calendarPermissions | read | calendar permissions | List who a calendar of a specified user is shared with. |
| GET | v1.0/users/{id}/calendars/{id}/calendarPermissions/{id} | read | calendar permissions | Get a sharing permission of a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/calendarPermissions | write | calendar permissions | Share a calendar of a specified user with a user or delegate. |
| PATCH | v1.0/users/{id}/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Change a sharing permission on a calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Remove a sharing permission from a calendar of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/calendarPermissions | read | calendar permissions | List who a calendar of a specified user is shared with. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id} | read | calendar permissions | Get a sharing permission of a calendar of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/calendarPermissions | write | calendar permissions | Share a calendar of a specified user with a user or delegate. |
| PATCH | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Change a sharing permission on a calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/calendarPermissions/{id} | write | calendar permissions | Remove a sharing permission from a calendar of a specified user. |
| GET | `v1.0/me/events/**` | read | events | Read anything under the events of the signed-in user: events, instances, attachments, extensions, delta, $count. |
| GET | v1.0/me/events | read | events | List events in the calendars of the signed-in user. |
| GET | v1.0/me/events/delta | read | events | Track event changes in the calendars of the signed-in user (delta query). |
| GET | v1.0/me/events/{id} | read | events | Get an event in the calendars of the signed-in user. |
| GET | v1.0/me/events/{id}/instances | read | events | List the occurrences of a recurring event in the calendars of the signed-in user. |
| POST | v1.0/me/events | write | events | Create an event in the calendars of the signed-in user; invitations are sent to any attendees. |
| PATCH | v1.0/me/events/{id} | write | events | Update an event in the calendars of the signed-in user. |
| DELETE | v1.0/me/events/{id} | write | events | Delete an event in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/accept | write | events | Accept an event invitation in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/decline | write | events | Decline an event invitation in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/cancel | write | events | Cancel an event and notify attendees in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/forward | write | events | Forward an event to new recipients in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/permanentDelete | write | events | Permanently delete an event in the calendars of the signed-in user. |
| GET | v1.0/me/calendar/events | read | events | List events in the default calendar of the signed-in user. |
| GET | v1.0/me/calendar/events/delta | read | events | Track event changes in the default calendar of the signed-in user (delta query). |
| GET | v1.0/me/calendar/events/{id} | read | events | Get an event in the default calendar of the signed-in user. |
| GET | v1.0/me/calendar/events/{id}/instances | read | events | List the occurrences of a recurring event in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events | write | events | Create an event in the default calendar of the signed-in user; invitations are sent to any attendees. |
| PATCH | v1.0/me/calendar/events/{id} | write | events | Update an event in the default calendar of the signed-in user. |
| DELETE | v1.0/me/calendar/events/{id} | write | events | Delete an event in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/accept | write | events | Accept an event invitation in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/decline | write | events | Decline an event invitation in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/cancel | write | events | Cancel an event and notify attendees in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/forward | write | events | Forward an event to new recipients in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/permanentDelete | write | events | Permanently delete an event in the default calendar of the signed-in user. |
| GET | v1.0/me/calendars/{id}/events | read | events | List events in a calendar of the signed-in user. |
| GET | v1.0/me/calendars/{id}/events/delta | read | events | Track event changes in a calendar of the signed-in user (delta query). |
| GET | v1.0/me/calendars/{id}/events/{id} | read | events | Get an event in a calendar of the signed-in user. |
| GET | v1.0/me/calendars/{id}/events/{id}/instances | read | events | List the occurrences of a recurring event in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events | write | events | Create an event in a calendar of the signed-in user; invitations are sent to any attendees. |
| PATCH | v1.0/me/calendars/{id}/events/{id} | write | events | Update an event in a calendar of the signed-in user. |
| DELETE | v1.0/me/calendars/{id}/events/{id} | write | events | Delete an event in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/accept | write | events | Accept an event invitation in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/decline | write | events | Decline an event invitation in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/cancel | write | events | Cancel an event and notify attendees in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/forward | write | events | Forward an event to new recipients in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/permanentDelete | write | events | Permanently delete an event in a calendar of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/events | read | events | List events in a calendar of a calendar group of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/events/delta | read | events | Track event changes in a calendar of a calendar group of the signed-in user (delta query). |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id} | read | events | Get an event in a calendar of a calendar group of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/instances | read | events | List the occurrences of a recurring event in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events | write | events | Create an event in a calendar of a calendar group of the signed-in user; invitations are sent to any attendees. |
| PATCH | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id} | write | events | Update an event in a calendar of a calendar group of the signed-in user. |
| DELETE | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id} | write | events | Delete an event in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/accept | write | events | Accept an event invitation in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/decline | write | events | Decline an event invitation in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/cancel | write | events | Cancel an event and notify attendees in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/forward | write | events | Forward an event to new recipients in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/permanentDelete | write | events | Permanently delete an event in a calendar of a calendar group of the signed-in user. |
| GET | `v1.0/users/{id}/events/**` | read | events | Read anything under the events of a specified user: events, instances, attachments, extensions, delta, $count. |
| GET | v1.0/users/{id}/events | read | events | List events in the calendars of a specified user. |
| GET | v1.0/users/{id}/events/delta | read | events | Track event changes in the calendars of a specified user (delta query). |
| GET | v1.0/users/{id}/events/{id} | read | events | Get an event in the calendars of a specified user. |
| GET | v1.0/users/{id}/events/{id}/instances | read | events | List the occurrences of a recurring event in the calendars of a specified user. |
| POST | v1.0/users/{id}/events | write | events | Create an event in the calendars of a specified user; invitations are sent to any attendees. |
| PATCH | v1.0/users/{id}/events/{id} | write | events | Update an event in the calendars of a specified user. |
| DELETE | v1.0/users/{id}/events/{id} | write | events | Delete an event in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/accept | write | events | Accept an event invitation in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/decline | write | events | Decline an event invitation in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/cancel | write | events | Cancel an event and notify attendees in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/forward | write | events | Forward an event to new recipients in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/permanentDelete | write | events | Permanently delete an event in the calendars of a specified user. |
| GET | v1.0/users/{id}/calendar/events | read | events | List events in the default calendar of a specified user. |
| GET | v1.0/users/{id}/calendar/events/delta | read | events | Track event changes in the default calendar of a specified user (delta query). |
| GET | v1.0/users/{id}/calendar/events/{id} | read | events | Get an event in the default calendar of a specified user. |
| GET | v1.0/users/{id}/calendar/events/{id}/instances | read | events | List the occurrences of a recurring event in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events | write | events | Create an event in the default calendar of a specified user; invitations are sent to any attendees. |
| PATCH | v1.0/users/{id}/calendar/events/{id} | write | events | Update an event in the default calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendar/events/{id} | write | events | Delete an event in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/accept | write | events | Accept an event invitation in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/decline | write | events | Decline an event invitation in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/cancel | write | events | Cancel an event and notify attendees in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/forward | write | events | Forward an event to new recipients in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/permanentDelete | write | events | Permanently delete an event in the default calendar of a specified user. |
| GET | v1.0/users/{id}/calendars/{id}/events | read | events | List events in a calendar of a specified user. |
| GET | v1.0/users/{id}/calendars/{id}/events/delta | read | events | Track event changes in a calendar of a specified user (delta query). |
| GET | v1.0/users/{id}/calendars/{id}/events/{id} | read | events | Get an event in a calendar of a specified user. |
| GET | v1.0/users/{id}/calendars/{id}/events/{id}/instances | read | events | List the occurrences of a recurring event in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events | write | events | Create an event in a calendar of a specified user; invitations are sent to any attendees. |
| PATCH | v1.0/users/{id}/calendars/{id}/events/{id} | write | events | Update an event in a calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendars/{id}/events/{id} | write | events | Delete an event in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/accept | write | events | Accept an event invitation in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/decline | write | events | Decline an event invitation in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/cancel | write | events | Cancel an event and notify attendees in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/forward | write | events | Forward an event to new recipients in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/permanentDelete | write | events | Permanently delete an event in a calendar of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events | read | events | List events in a calendar of a calendar group of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/delta | read | events | Track event changes in a calendar of a calendar group of a specified user (delta query). |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id} | read | events | Get an event in a calendar of a calendar group of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/instances | read | events | List the occurrences of a recurring event in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events | write | events | Create an event in a calendar of a calendar group of a specified user; invitations are sent to any attendees. |
| PATCH | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id} | write | events | Update an event in a calendar of a calendar group of a specified user. |
| DELETE | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id} | write | events | Delete an event in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/accept | write | events | Accept an event invitation in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/decline | write | events | Decline an event invitation in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/tentativelyAccept | write | events | Tentatively accept an event invitation in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/cancel | write | events | Cancel an event and notify attendees in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/forward | write | events | Forward an event to new recipients in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/dismissReminder | write | events | Dismiss the reminder of an event in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/snoozeReminder | write | events | Snooze the reminder of an event in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/permanentDelete | write | events | Permanently delete an event in a calendar of a calendar group of a specified user. |
| GET | v1.0/me/events/{id}/attachments | read | event attachments | List attachments of an event in the calendars of the signed-in user. |
| GET | v1.0/me/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/attachments | write | event attachments | Add an attachment to an event in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in the calendars of the signed-in user. |
| DELETE | v1.0/me/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in the calendars of the signed-in user. |
| GET | v1.0/me/calendar/events/{id}/attachments | read | event attachments | List attachments of an event in the default calendar of the signed-in user. |
| GET | v1.0/me/calendar/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/attachments | write | event attachments | Add an attachment to an event in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in the default calendar of the signed-in user. |
| DELETE | v1.0/me/calendar/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in the default calendar of the signed-in user. |
| GET | v1.0/me/calendars/{id}/events/{id}/attachments | read | event attachments | List attachments of an event in a calendar of the signed-in user. |
| GET | v1.0/me/calendars/{id}/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/attachments | write | event attachments | Add an attachment to an event in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in a calendar of the signed-in user. |
| DELETE | v1.0/me/calendars/{id}/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in a calendar of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/attachments | read | event attachments | List attachments of an event in a calendar of a calendar group of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/attachments | write | event attachments | Add an attachment to an event in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in a calendar of a calendar group of the signed-in user. |
| DELETE | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in a calendar of a calendar group of the signed-in user. |
| GET | v1.0/users/{id}/events/{id}/attachments | read | event attachments | List attachments of an event in the calendars of a specified user. |
| GET | v1.0/users/{id}/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/attachments | write | event attachments | Add an attachment to an event in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in the calendars of a specified user. |
| DELETE | v1.0/users/{id}/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in the calendars of a specified user. |
| GET | v1.0/users/{id}/calendar/events/{id}/attachments | read | event attachments | List attachments of an event in the default calendar of a specified user. |
| GET | v1.0/users/{id}/calendar/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/attachments | write | event attachments | Add an attachment to an event in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in the default calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendar/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in the default calendar of a specified user. |
| GET | v1.0/users/{id}/calendars/{id}/events/{id}/attachments | read | event attachments | List attachments of an event in a calendar of a specified user. |
| GET | v1.0/users/{id}/calendars/{id}/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/attachments | write | event attachments | Add an attachment to an event in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in a calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendars/{id}/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in a calendar of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/attachments | read | event attachments | List attachments of an event in a calendar of a calendar group of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/{id} | read | event attachments | Get an attachment of an event in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/attachments | write | event attachments | Add an attachment to an event in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/createUploadSession | write | event attachments | Create an upload session to attach a large file to an event in a calendar of a calendar group of a specified user. |
| DELETE | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/attachments/{id} | write | event attachments | Delete an attachment from an event in a calendar of a calendar group of a specified user. |
| GET | v1.0/me/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in the calendars of the signed-in user. |
| POST | v1.0/me/events/{id}/extensions | write | event extensions | Create an open extension on an event in the calendars of the signed-in user. |
| PATCH | v1.0/me/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in the calendars of the signed-in user. |
| DELETE | v1.0/me/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in the calendars of the signed-in user. |
| GET | v1.0/me/calendar/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in the default calendar of the signed-in user. |
| POST | v1.0/me/calendar/events/{id}/extensions | write | event extensions | Create an open extension on an event in the default calendar of the signed-in user. |
| PATCH | v1.0/me/calendar/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in the default calendar of the signed-in user. |
| DELETE | v1.0/me/calendar/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in the default calendar of the signed-in user. |
| GET | v1.0/me/calendars/{id}/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in a calendar of the signed-in user. |
| POST | v1.0/me/calendars/{id}/events/{id}/extensions | write | event extensions | Create an open extension on an event in a calendar of the signed-in user. |
| PATCH | v1.0/me/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in a calendar of the signed-in user. |
| DELETE | v1.0/me/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in a calendar of the signed-in user. |
| GET | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in a calendar of a calendar group of the signed-in user. |
| POST | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/extensions | write | event extensions | Create an open extension on an event in a calendar of a calendar group of the signed-in user. |
| PATCH | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in a calendar of a calendar group of the signed-in user. |
| DELETE | v1.0/me/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in a calendar of a calendar group of the signed-in user. |
| GET | v1.0/users/{id}/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in the calendars of a specified user. |
| POST | v1.0/users/{id}/events/{id}/extensions | write | event extensions | Create an open extension on an event in the calendars of a specified user. |
| PATCH | v1.0/users/{id}/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in the calendars of a specified user. |
| DELETE | v1.0/users/{id}/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in the calendars of a specified user. |
| GET | v1.0/users/{id}/calendar/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in the default calendar of a specified user. |
| POST | v1.0/users/{id}/calendar/events/{id}/extensions | write | event extensions | Create an open extension on an event in the default calendar of a specified user. |
| PATCH | v1.0/users/{id}/calendar/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in the default calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendar/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in the default calendar of a specified user. |
| GET | v1.0/users/{id}/calendars/{id}/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in a calendar of a specified user. |
| POST | v1.0/users/{id}/calendars/{id}/events/{id}/extensions | write | event extensions | Create an open extension on an event in a calendar of a specified user. |
| PATCH | v1.0/users/{id}/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in a calendar of a specified user. |
| DELETE | v1.0/users/{id}/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in a calendar of a specified user. |
| GET | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id} | read | event extensions | Get an open extension of an event in a calendar of a calendar group of a specified user. |
| POST | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/extensions | write | event extensions | Create an open extension on an event in a calendar of a calendar group of a specified user. |
| PATCH | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Update an open extension of an event in a calendar of a calendar group of a specified user. |
| DELETE | v1.0/users/{id}/calendarGroups/{id}/calendars/{id}/events/{id}/extensions/{id} | write | event extensions | Delete an open extension of an event in a calendar of a calendar group of a specified user. |
| GET | `v1.0/me/contacts/**` | read | contacts | Read anything under the contacts of the signed-in user: contacts, photos, extensions, delta, $count. |
| GET | v1.0/me/contacts | read | contacts | List contacts in the default folder of the signed-in user. |
| GET | v1.0/me/contacts/delta | read | contacts | Track contact changes in the default folder of the signed-in user (delta query). |
| GET | v1.0/me/contacts/{id} | read | contacts | Get a contact in the default folder of the signed-in user. |
| GET | v1.0/me/contacts/{id}/photo | read | contacts | Get photo metadata of a contact in the default folder of the signed-in user. |
| GET | v1.0/me/contacts/{id}/photo/$value | read | contacts | Download the photo of a contact in the default folder of the signed-in user. |
| POST | v1.0/me/contacts | write | contacts | Create a contact in the default folder of the signed-in user. |
| PATCH | v1.0/me/contacts/{id} | write | contacts | Update a contact in the default folder of the signed-in user. |
| DELETE | v1.0/me/contacts/{id} | write | contacts | Delete a contact in the default folder of the signed-in user. |
| POST | v1.0/me/contacts/{id}/permanentDelete | write | contacts | Permanently delete a contact in the default folder of the signed-in user. |
| PUT | v1.0/me/contacts/{id}/photo/$value | write | contacts | Replace the photo of a contact in the default folder of the signed-in user. |
| PATCH | v1.0/me/contacts/{id}/photo | write | contacts | Update the photo of a contact in the default folder of the signed-in user. |
| POST | v1.0/me/contacts/{id}/extensions | write | contacts | Create an open extension on a contact in the default folder of the signed-in user. |
| PATCH | v1.0/me/contacts/{id}/extensions/{id} | write | contacts | Update an open extension of a contact in the default folder of the signed-in user. |
| DELETE | v1.0/me/contacts/{id}/extensions/{id} | write | contacts | Delete an open extension of a contact in the default folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/contacts | read | contacts | List contacts in a contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/contacts/delta | read | contacts | Track contact changes in a contact folder of the signed-in user (delta query). |
| GET | v1.0/me/contactFolders/{id}/contacts/{id} | read | contacts | Get a contact in a contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/contacts/{id}/photo | read | contacts | Get photo metadata of a contact in a contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/contacts/{id}/photo/$value | read | contacts | Download the photo of a contact in a contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/contacts | write | contacts | Create a contact in a contact folder of the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id}/contacts/{id} | write | contacts | Update a contact in a contact folder of the signed-in user. |
| DELETE | v1.0/me/contactFolders/{id}/contacts/{id} | write | contacts | Delete a contact in a contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/contacts/{id}/permanentDelete | write | contacts | Permanently delete a contact in a contact folder of the signed-in user. |
| PUT | v1.0/me/contactFolders/{id}/contacts/{id}/photo/$value | write | contacts | Replace the photo of a contact in a contact folder of the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id}/contacts/{id}/photo | write | contacts | Update the photo of a contact in a contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/contacts/{id}/extensions | write | contacts | Create an open extension on a contact in a contact folder of the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Update an open extension of a contact in a contact folder of the signed-in user. |
| DELETE | v1.0/me/contactFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Delete an open extension of a contact in a contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts | read | contacts | List contacts in a child contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/delta | read | contacts | Track contact changes in a child contact folder of the signed-in user (delta query). |
| GET | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id} | read | contacts | Get a contact in a child contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo | read | contacts | Get photo metadata of a contact in a child contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo/$value | read | contacts | Download the photo of a contact in a child contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts | write | contacts | Create a contact in a child contact folder of the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id} | write | contacts | Update a contact in a child contact folder of the signed-in user. |
| DELETE | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id} | write | contacts | Delete a contact in a child contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/permanentDelete | write | contacts | Permanently delete a contact in a child contact folder of the signed-in user. |
| PUT | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo/$value | write | contacts | Replace the photo of a contact in a child contact folder of the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo | write | contacts | Update the photo of a contact in a child contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/extensions | write | contacts | Create an open extension on a contact in a child contact folder of the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Update an open extension of a contact in a child contact folder of the signed-in user. |
| DELETE | v1.0/me/contactFolders/{id}/childFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Delete an open extension of a contact in a child contact folder of the signed-in user. |
| GET | `v1.0/users/{id}/contacts/**` | read | contacts | Read anything under the contacts of a specified user: contacts, photos, extensions, delta, $count. |
| GET | v1.0/users/{id}/contacts | read | contacts | List contacts in the default folder of a specified user. |
| GET | v1.0/users/{id}/contacts/delta | read | contacts | Track contact changes in the default folder of a specified user (delta query). |
| GET | v1.0/users/{id}/contacts/{id} | read | contacts | Get a contact in the default folder of a specified user. |
| GET | v1.0/users/{id}/contacts/{id}/photo | read | contacts | Get photo metadata of a contact in the default folder of a specified user. |
| GET | v1.0/users/{id}/contacts/{id}/photo/$value | read | contacts | Download the photo of a contact in the default folder of a specified user. |
| POST | v1.0/users/{id}/contacts | write | contacts | Create a contact in the default folder of a specified user. |
| PATCH | v1.0/users/{id}/contacts/{id} | write | contacts | Update a contact in the default folder of a specified user. |
| DELETE | v1.0/users/{id}/contacts/{id} | write | contacts | Delete a contact in the default folder of a specified user. |
| POST | v1.0/users/{id}/contacts/{id}/permanentDelete | write | contacts | Permanently delete a contact in the default folder of a specified user. |
| PUT | v1.0/users/{id}/contacts/{id}/photo/$value | write | contacts | Replace the photo of a contact in the default folder of a specified user. |
| PATCH | v1.0/users/{id}/contacts/{id}/photo | write | contacts | Update the photo of a contact in the default folder of a specified user. |
| POST | v1.0/users/{id}/contacts/{id}/extensions | write | contacts | Create an open extension on a contact in the default folder of a specified user. |
| PATCH | v1.0/users/{id}/contacts/{id}/extensions/{id} | write | contacts | Update an open extension of a contact in the default folder of a specified user. |
| DELETE | v1.0/users/{id}/contacts/{id}/extensions/{id} | write | contacts | Delete an open extension of a contact in the default folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/contacts | read | contacts | List contacts in a contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/contacts/delta | read | contacts | Track contact changes in a contact folder of a specified user (delta query). |
| GET | v1.0/users/{id}/contactFolders/{id}/contacts/{id} | read | contacts | Get a contact in a contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/photo | read | contacts | Get photo metadata of a contact in a contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/photo/$value | read | contacts | Download the photo of a contact in a contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/contacts | write | contacts | Create a contact in a contact folder of a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id}/contacts/{id} | write | contacts | Update a contact in a contact folder of a specified user. |
| DELETE | v1.0/users/{id}/contactFolders/{id}/contacts/{id} | write | contacts | Delete a contact in a contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/permanentDelete | write | contacts | Permanently delete a contact in a contact folder of a specified user. |
| PUT | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/photo/$value | write | contacts | Replace the photo of a contact in a contact folder of a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/photo | write | contacts | Update the photo of a contact in a contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/extensions | write | contacts | Create an open extension on a contact in a contact folder of a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Update an open extension of a contact in a contact folder of a specified user. |
| DELETE | v1.0/users/{id}/contactFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Delete an open extension of a contact in a contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts | read | contacts | List contacts in a child contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/delta | read | contacts | Track contact changes in a child contact folder of a specified user (delta query). |
| GET | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id} | read | contacts | Get a contact in a child contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo | read | contacts | Get photo metadata of a contact in a child contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo/$value | read | contacts | Download the photo of a contact in a child contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts | write | contacts | Create a contact in a child contact folder of a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id} | write | contacts | Update a contact in a child contact folder of a specified user. |
| DELETE | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id} | write | contacts | Delete a contact in a child contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/permanentDelete | write | contacts | Permanently delete a contact in a child contact folder of a specified user. |
| PUT | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo/$value | write | contacts | Replace the photo of a contact in a child contact folder of a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/photo | write | contacts | Update the photo of a contact in a child contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/extensions | write | contacts | Create an open extension on a contact in a child contact folder of a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Update an open extension of a contact in a child contact folder of a specified user. |
| DELETE | v1.0/users/{id}/contactFolders/{id}/childFolders/{id}/contacts/{id}/extensions/{id} | write | contacts | Delete an open extension of a contact in a child contact folder of a specified user. |
| GET | `v1.0/me/contactFolders/**` | read | contact folders | Read anything under the contact folders of the signed-in user: folders, child folders and their contacts. |
| GET | v1.0/me/contactFolders | read | contact folders | List contact folders of the signed-in user. |
| GET | v1.0/me/contactFolders/delta | read | contact folders | Track contact folder changes of the signed-in user (delta query). |
| GET | v1.0/me/contactFolders/{id} | read | contact folders | Get a contact folder of the signed-in user. |
| GET | v1.0/me/contactFolders/{id}/childFolders | read | contact folders | List child folders of a contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders | write | contact folders | Create a contact folder for the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/childFolders | write | contact folders | Create a child contact folder for the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id} | write | contact folders | Update a contact folder of the signed-in user. |
| DELETE | v1.0/me/contactFolders/{id} | write | contact folders | Delete a contact folder of the signed-in user. |
| POST | v1.0/me/contactFolders/{id}/permanentDelete | write | contact folders | Permanently delete a contact folder of the signed-in user. |
| PATCH | v1.0/me/contactFolders/{id}/childFolders/{id} | write | contact folders | Update a child contact folder of the signed-in user. |
| DELETE | v1.0/me/contactFolders/{id}/childFolders/{id} | write | contact folders | Delete a child contact folder of the signed-in user. |
| GET | `v1.0/users/{id}/contactFolders/**` | read | contact folders | Read anything under the contact folders of a specified user: folders, child folders and their contacts. |
| GET | v1.0/users/{id}/contactFolders | read | contact folders | List contact folders of a specified user. |
| GET | v1.0/users/{id}/contactFolders/delta | read | contact folders | Track contact folder changes of a specified user (delta query). |
| GET | v1.0/users/{id}/contactFolders/{id} | read | contact folders | Get a contact folder of a specified user. |
| GET | v1.0/users/{id}/contactFolders/{id}/childFolders | read | contact folders | List child folders of a contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders | write | contact folders | Create a contact folder for a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/childFolders | write | contact folders | Create a child contact folder for a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id} | write | contact folders | Update a contact folder of a specified user. |
| DELETE | v1.0/users/{id}/contactFolders/{id} | write | contact folders | Delete a contact folder of a specified user. |
| POST | v1.0/users/{id}/contactFolders/{id}/permanentDelete | write | contact folders | Permanently delete a contact folder of a specified user. |
| PATCH | v1.0/users/{id}/contactFolders/{id}/childFolders/{id} | write | contact folders | Update a child contact folder of a specified user. |
| DELETE | v1.0/users/{id}/contactFolders/{id}/childFolders/{id} | write | contact folders | Delete a child contact folder of a specified user. |
| POST | v1.0/search/query | read | search | Run a Microsoft Search query (messages, events and other entity types); POST only carries the query. |
| POST | v1.0/$batch | write | batch | JSON batch of up to 20 Graph requests; can carry writes, so it is not part of read access. |
| GET | v1.0/subscriptions | read | subscriptions | List change-notification (webhook) subscriptions; clientState is not returned. |
| GET | v1.0/subscriptions/{id} | read | subscriptions | Get a change-notification subscription. |
| POST | v1.0/subscriptions | write | subscriptions | Create a webhook subscription that pushes mail, calendar or contact changes to an external URL. |
| PATCH | v1.0/subscriptions/{id} | write | subscriptions | Renew or update a webhook subscription. |
| DELETE | v1.0/subscriptions/{id} | write | subscriptions | Delete a webhook subscription. |
| POST | v1.0/subscriptions/{id}/reauthorize | write | subscriptions | Reauthorize a webhook subscription after a lifecycle notification. |
