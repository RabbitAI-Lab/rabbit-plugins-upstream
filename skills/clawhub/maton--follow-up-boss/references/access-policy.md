# Follow Up Boss access policy

An access policy limits which endpoints Follow Up Boss connections may call through Maton. Follow Up Boss doesn't offer a choice of OAuth scopes, so an access policy is the way to narrow a connection. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/follow-up-boss#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Follow Up Boss: its 66 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create follow-up-boss --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "v1/actionPlans"},
    {"method": "GET", "path": "v1/actionPlansPeople"},
    {"method": "GET", "path": "v1/appointmentOutcomes"},
    {"method": "GET", "path": "v1/appointmentOutcomes/{id}"},
    {"method": "GET", "path": "v1/appointmentTypes"},
    {"method": "GET", "path": "v1/appointmentTypes/{id}"},
    {"method": "GET", "path": "v1/appointments"},
    {"method": "GET", "path": "v1/appointments/{id}"},
    {"method": "GET", "path": "v1/automations"},
    {"method": "GET", "path": "v1/automations/{id}"},
    {"method": "GET", "path": "v1/automationsPeople"},
    {"method": "GET", "path": "v1/automationsPeople/{id}"},
    {"method": "GET", "path": "v1/calls"},
    {"method": "GET", "path": "v1/calls/{id}"},
    {"method": "GET", "path": "v1/customFields"},
    {"method": "GET", "path": "v1/customFields/{id}"},
    {"method": "GET", "path": "v1/dealAttachments/{id}"},
    {"method": "GET", "path": "v1/deals"},
    {"method": "GET", "path": "v1/deals/{id}"},
    {"method": "GET", "path": "v1/dealCustomFields"},
    {"method": "GET", "path": "v1/dealCustomFields/{id}"},
    {"method": "GET", "path": "v1/emCampaigns"},
    {"method": "GET", "path": "v1/emEvents"},
    {"method": "GET", "path": "v1/templates"},
    {"method": "GET", "path": "v1/templates/{id}"},
    {"method": "GET", "path": "v1/events"},
    {"method": "GET", "path": "v1/events/{id}"},
    {"method": "GET", "path": "v1/groups"},
    {"method": "GET", "path": "v1/groups/roundRobin"},
    {"method": "GET", "path": "v1/groups/{id}"},
    {"method": "GET", "path": "v1/identity"},
    {"method": "GET", "path": "v1/inboxApps/installedApps/{id}"},
    {"method": "GET", "path": "v1/inboxApps/{id}/conversations/{id}/participants"},
    {"method": "GET", "path": "v1/notes/{id}"},
    {"method": "GET", "path": "v1/people"},
    {"method": "GET", "path": "v1/people/checkDuplicate"},
    {"method": "GET", "path": "v1/people/unclaimed"},
    {"method": "GET", "path": "v1/people/{id}"},
    {"method": "GET", "path": "v1/personAttachments/{id}"},
    {"method": "GET", "path": "v1/peopleRelationships"},
    {"method": "GET", "path": "v1/peopleRelationships/{id}"},
    {"method": "GET", "path": "v1/pipelines"},
    {"method": "GET", "path": "v1/pipelines/{id}"},
    {"method": "GET", "path": "v1/ponds"},
    {"method": "GET", "path": "v1/ponds/{id}"},
    {"method": "GET", "path": "v1/reactions/{id}"},
    {"method": "GET", "path": "v1/smartLists"},
    {"method": "GET", "path": "v1/smartLists/{id}"},
    {"method": "GET", "path": "v1/stages"},
    {"method": "GET", "path": "v1/stages/{id}"},
    {"method": "GET", "path": "v1/tasks"},
    {"method": "GET", "path": "v1/tasks/{id}"},
    {"method": "GET", "path": "v1/teamInboxes"},
    {"method": "GET", "path": "v1/teams"},
    {"method": "GET", "path": "v1/teams/{id}"},
    {"method": "GET", "path": "v1/textMessageTemplates"},
    {"method": "GET", "path": "v1/textMessageTemplates/{id}"},
    {"method": "GET", "path": "v1/textMessages"},
    {"method": "GET", "path": "v1/textMessages/{id}"},
    {"method": "GET", "path": "v1/threadedReplies/{id}"},
    {"method": "GET", "path": "v1/timeframes"},
    {"method": "GET", "path": "v1/users"},
    {"method": "GET", "path": "v1/users/{id}"},
    {"method": "GET", "path": "v1/webhookEvents/{id}"},
    {"method": "GET", "path": "v1/webhooks"},
    {"method": "GET", "path": "v1/webhooks/{id}"}
  ],
  "deny": []
}
```

## Endpoints

The Follow Up Boss endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | v1/actionPlans | read | action plans | Get a list of Action Plans. |
| GET | v1/actionPlansPeople | read | action plans | List Action Plans applied to a particular person or list people on a particular Action Plan. |
| POST | v1/actionPlansPeople | write | action plans | Apply an Action Plan to a person. |
| PUT | v1/actionPlansPeople/{id} | write | action plans | Update the status of an Action Plan to Person relationship. |
| GET | v1/appointmentOutcomes | read | appointment outcomes | List appointment outcomes. |
| POST | v1/appointmentOutcomes | write | appointment outcomes | Create an appointment outcome. |
| GET | v1/appointmentOutcomes/{id} | read | appointment outcomes | Retrieve an appointment outcome by ID. |
| PUT | v1/appointmentOutcomes/{id} | write | appointment outcomes | Update an appointment outcome. |
| DELETE | v1/appointmentOutcomes/{id} | write | appointment outcomes | Delete an appointment outcome. |
| GET | v1/appointmentTypes | read | appointment types | List appointment types. |
| POST | v1/appointmentTypes | write | appointment types | Create an appointment type. |
| GET | v1/appointmentTypes/{id} | read | appointment types | Retrieve an appointment type by ID. |
| PUT | v1/appointmentTypes/{id} | write | appointment types | Update an appointment type. |
| DELETE | v1/appointmentTypes/{id} | write | appointment types | Delete an appointment type. |
| GET | v1/appointments | read | appointments | Search for appointments. |
| POST | v1/appointments | write | appointments | Create an appointment. |
| GET | v1/appointments/{id} | read | appointments | Retrieve an appointment by id. |
| PUT | v1/appointments/{id} | write | appointments | Update an appointment. |
| DELETE | v1/appointments/{id} | write | appointments | Delete an appointment. |
| GET | v1/automations | read | automations | Get a list of Automations. |
| GET | v1/automations/{id} | read | automations | Retrieve an Automation by ID. |
| GET | v1/automationsPeople | read | automations | Get a list of pairings of Automations and the People on which they have or will be run. |
| POST | v1/automationsPeople | write | automations | Manually trigger an Automation for a specified Person. |
| GET | v1/automationsPeople/{id} | read | automations | Retrieve an Automation-Person pairing. |
| PUT | v1/automationsPeople/{id} | write | automations | Pause or unpause an Automation for a Person. |
| GET | v1/calls | read | calls | Search for calls. |
| POST | v1/calls | write | calls | Add a call. |
| GET | v1/calls/{id} | read | calls | Retrieve a call by id. |
| PUT | v1/calls/{id} | write | calls | Update a call. |
| GET | v1/customFields | read | custom fields | List all custom fields. |
| POST | v1/customFields | write | custom fields | Create a custom field. |
| GET | v1/customFields/{id} | read | custom fields | Get a custom field by id. |
| PUT | v1/customFields/{id} | write | custom fields | Update a custom field. |
| DELETE | v1/customFields/{id} | write | custom fields | Delete a custom field. |
| POST | v1/dealAttachments | write | deals | Add an attachment to a deal. |
| GET | v1/dealAttachments/{id} | read | deals | Get a deal attachment by id. |
| PUT | v1/dealAttachments/{id} | write | deals | Update a deal attachment. |
| DELETE | v1/dealAttachments/{id} | write | deals | Delete a deal attachment. |
| GET | v1/deals | read | deals | Search for deals. |
| POST | v1/deals | write | deals | Add a deal. |
| GET | v1/deals/{id} | read | deals | Retrieve a deal by id. |
| PUT | v1/deals/{id} | write | deals | Update a deal. |
| DELETE | v1/deals/{id} | write | deals | Delete a deal. |
| GET | v1/dealCustomFields | read | deals custom fields | List all deals custom fields available in your account. |
| POST | v1/dealCustomFields | write | deals custom fields | Create a deals custom field. |
| GET | v1/dealCustomFields/{id} | read | deals custom fields | Get a deals custom field by ID. |
| PUT | v1/dealCustomFields/{id} | write | deals custom fields | Update a deals custom field. |
| DELETE | v1/dealCustomFields/{id} | write | deals custom fields | Delete a deals custom field. |
| GET | v1/emCampaigns | read | email marketing | List email marketing campaigns. |
| POST | v1/emCampaigns | write | email marketing | Create an email marketing campaign. |
| PUT | v1/emCampaigns/{id} | write | email marketing | Update an email marketing campaign. |
| GET | v1/emEvents | read | email marketing | List email marketing events. |
| POST | v1/emEvents | write | email marketing | Notify Follow Up Boss about marketing emails sent, opens, clicks, bounces, unsubscribes and spam reports. |
| GET | v1/templates | read | email templates | Lists all email templates. |
| POST | v1/templates | write | email templates | Create a new email template. |
| POST | v1/templates/merge | write | email templates | Merge an email template with multiple recipients. |
| GET | v1/templates/{id} | read | email templates | Retrieve an email template by id, optionally merging fields. |
| PUT | v1/templates/{id} | write | email templates | Update an email template. |
| DELETE | v1/templates/{id} | write | email templates | Delete an email template. |
| GET | v1/events | read | events | Search for events. |
| POST | v1/events | write | events | Send in a lead or an event related to a lead. |
| GET | v1/events/{id} | read | events | Retrieve a single event by id. |
| GET | v1/groups | read | groups | List groups. |
| POST | v1/groups | write | groups | Create a new group. |
| GET | v1/groups/roundRobin | read | groups | Lists groups and includes round-robin data. |
| GET | v1/groups/{id} | read | groups | Retrieve a group by id. |
| PUT | v1/groups/{id} | write | groups | Update a group. |
| DELETE | v1/groups/{id} | write | groups | Delete a group. |
| GET | v1/identity | read | identity | Get identity and authentication information. |
| POST | v1/inboxApps/install | write | inbox apps | Installs your Inbox App for an account. |
| GET | v1/inboxApps/installedApps/{id} | read | inbox apps | Lists Inbox App installation(s) and ID(s) for your Published Inbox App on the current FUB account. |
| DELETE | v1/inboxApps/{id} | write | inbox apps | Deactivates an installation of your Inbox App. |
| PUT | v1/inboxApps/{id}/conversations/{id} | write | inbox apps | Updates an Inbox App conversation. |
| GET | v1/inboxApps/{id}/conversations/{id}/participants | read | inbox apps | Retrieves participants in an Inbox App conversation. |
| POST | v1/inboxApps/{id}/conversations/{id}/participants | write | inbox apps | Adds a participant to an Inbox App conversation. |
| DELETE | v1/inboxApps/{id}/conversations/{id}/participants/{id} | write | inbox apps | Deletes an Inbox App conversation participant. |
| POST | v1/inboxApps/{id}/message | write | inbox apps | Adds a message to an existing or new Inbox App conversation. |
| PUT | v1/inboxApps/{id}/message | write | inbox apps | Update an Inbox App Message. |
| POST | v1/inboxApps/{id}/note | write | inbox apps | Adds a note to an Inbox App conversation. |
| POST | v1/inboxApps/{id}/systemMessage | write | inbox apps | Adds a system confirmation message to an existing or new Inbox App conversation. |
| POST | v1/notes | write | notes | Add a note. |
| GET | v1/notes/{id} | read | notes | Retrieve a note by id. |
| PUT | v1/notes/{id} | write | notes | Edit a note. |
| DELETE | v1/notes/{id} | write | notes | Delete a note. |
| GET | v1/people | read | people | Search for people. |
| POST | v1/people | write | people | Manually add a new person. |
| GET | v1/people/checkDuplicate | read | people | Check whether a person exists in Follow Up Boss. |
| POST | v1/people/claim | write | people | Claim a lead. |
| POST | v1/people/ignoreUnclaimed | write | people | Ignore a lead. |
| GET | v1/people/unclaimed | read | people | Get unclaimed leads. |
| GET | v1/people/{id} | read | people | Retrieve a person by id. |
| PUT | v1/people/{id} | write | people | Update a person by id. |
| DELETE | v1/people/{id} | write | people | Delete a person by id. |
| POST | v1/personAttachments | write | people | Attach a file to a person. |
| GET | v1/personAttachments/{id} | read | people | Retrieve an attachment by ID. |
| PUT | v1/personAttachments/{id} | write | people | Update an attachment by ID. |
| DELETE | v1/personAttachments/{id} | write | people | Delete an attachment by ID. |
| GET | v1/peopleRelationships | read | people relationships | Get relationships between people in Follow Up Boss. |
| POST | v1/peopleRelationships | write | people relationships | Create a new relationship for a person. |
| GET | v1/peopleRelationships/{id} | read | people relationships | Get a specific relationship. |
| PUT | v1/peopleRelationships/{id} | write | people relationships | Update details of a specific relationship. |
| DELETE | v1/peopleRelationships/{id} | write | people relationships | Delete a relationship. |
| GET | v1/pipelines | read | pipelines | Search for pipelines. |
| POST | v1/pipelines | write | pipelines | Add a pipeline. |
| GET | v1/pipelines/{id} | read | pipelines | Retrieve a pipeline by id. |
| PUT | v1/pipelines/{id} | write | pipelines | Update a pipeline. |
| DELETE | v1/pipelines/{id} | write | pipelines | Delete a pipeline. |
| GET | v1/ponds | read | ponds | Get a list of ponds. |
| POST | v1/ponds | write | ponds | Create a pond. |
| GET | v1/ponds/{id} | read | ponds | Get a pond by id. |
| PUT | v1/ponds/{id} | write | ponds | Update a pond by id. |
| DELETE | v1/ponds/{id} | write | ponds | Delete a pond by id. |
| GET | v1/reactions/{id} | read | reactions | Fetch a reaction. |
| POST | v1/reactions/{id}/{id} | write | reactions | Add a reaction to a note, call or other object. |
| DELETE | v1/reactions/{id}/{id} | write | reactions | Delete a reaction. |
| GET | v1/smartLists | read | smart lists | Get a list of Smart Lists. |
| GET | v1/smartLists/{id} | read | smart lists | Retrieve a Smart List by id. |
| GET | v1/stages | read | stages | Retrieve a list of stages. |
| POST | v1/stages | write | stages | Create a new stage. |
| GET | v1/stages/{id} | read | stages | Get a stage by id. |
| PUT | v1/stages/{id} | write | stages | Update a stage. |
| DELETE | v1/stages/{id} | write | stages | Delete a stage. |
| GET | v1/tasks | read | tasks | Get a list of tasks. |
| POST | v1/tasks | write | tasks | Create a new task. |
| GET | v1/tasks/{id} | read | tasks | Get a task by id. |
| PUT | v1/tasks/{id} | write | tasks | Update a task. |
| DELETE | v1/tasks/{id} | write | tasks | Delete a task. |
| GET | v1/teamInboxes | read | team inboxes | Get a list of Team Inboxes. |
| GET | v1/teams | read | teams | Get a list of teams. |
| POST | v1/teams | write | teams | Create a new team. |
| GET | v1/teams/{id} | read | teams | Get a team by id. |
| PUT | v1/teams/{id} | write | teams | Update a team by id. |
| DELETE | v1/teams/{id} | write | teams | Delete a team by id. |
| GET | v1/textMessageTemplates | read | text message templates | Lists all text message templates. |
| POST | v1/textMessageTemplates | write | text message templates | Create a text message template. |
| POST | v1/textMessageTemplates/merge | write | text message templates | Merge a text message template with multiple recipients. |
| GET | v1/textMessageTemplates/{id} | read | text message templates | Retrieve a text message template by id. |
| PUT | v1/textMessageTemplates/{id} | write | text message templates | Update a text message template. |
| DELETE | v1/textMessageTemplates/{id} | write | text message templates | Delete a text message template. |
| GET | v1/textMessages | read | text messages | List text messages for a person or phone number. |
| POST | v1/textMessages | write | text messages | Create a record of an externally sent text message. |
| GET | v1/textMessages/{id} | read | text messages | Retrieve a text message by id. |
| GET | v1/threadedReplies/{id} | read | threaded replies | Fetches a threaded reply. |
| GET | v1/timeframes | read | timeframes | Get a list of timeframes. |
| GET | v1/users | read | users | Search for users. |
| GET | v1/users/{id} | read | users | Retrieve a user by id. |
| DELETE | v1/users/{id} | write | users | Delete a user. |
| GET | v1/webhookEvents/{id} | read | webhook events | Get a list of events for a given webhook. |
| GET | v1/webhooks | read | webhooks | Get a list of webhooks. |
| POST | v1/webhooks | write | webhooks | Subscribe to a new webhook. |
| GET | v1/webhooks/{id} | read | webhooks | Get details of a specific webhook. |
| PUT | v1/webhooks/{id} | write | webhooks | Update a webhook. |
| DELETE | v1/webhooks/{id} | write | webhooks | Delete a webhook. |
