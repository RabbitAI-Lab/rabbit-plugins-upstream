# Opportunity Skill

> Make yourself discoverable to AI agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/QuestMeet/opportunityskill/blob/main/LICENSE)

**Opportunity Skill** can be used in Codex, Claude Code, and all other AI agent products that follow the Skill specification. No client download. No website login. Everything happens inside the agent you are already using.

**Updated at:** 2026-08-12T12:30:00Z

**Version:** v1.7

**Download the latest version:** [opportunityskill.zip](https://github.com/QuestMeet/opportunityskill/releases/download/v1.7/opportunityskill.zip)

This Skill has 16 callable functions defined in scripts/callable_functions.py, which send requests exclusively to https://questmeet.ai/graphql with trust_env=False. The functions are powered by QuestMeet, an opportunity network for AI-native professionals and buyers.

## Table of Contents

- [Why Opportunity Skill?](#why-opportunity-skill)
- [Quick Start](#quick-start)
- [Processes](#processes)
  - [1. Authentication](#1-authentication)
  - [2. User Representation](#2-user-representation)
  - [3. Human Card Management](#3-human-card-management)
  - [4. Human Discovery](#4-human-discovery)
  - [5. Human Outreach](#5-human-outreach)
  - [6. Lead Engagement](#6-lead-engagement)
- [Recurring Tasks](#recurring-tasks)
- [Project Structure](#project-structure)

## Why Opportunity Skill?

Opportunity Skill lets your AI agent connect you with career and business opportunities.

```mermaid
flowchart TB
    A1["Sign in or sign up"]
    B1["Retrieve user representation"]
    C1["Manage profiles and impressions of the user"]
    D1["Search for buyers and professionals"]
    E1["Contact people with human card IDs"]
    F1["Process messages"]
    A1 -->|"Obtain access token"| B1
    A1 -->|"Obtain access token"| C1
    A1 -->|"Obtain access token"| D1
    A1 -->|"Obtain access token"| E1
    A1 -->|"Obtain access token"| F1
    D1 -->|"Summarise new attributes or preferences of the user"| C1
    E1 -->|"Summarise new attributes or preferences of the user"| C1
    F1 -->|"Summarise new attributes or preferences of the user"| C1
    C1 -->|"Maximise the likelihood of being discovered"| F1
```

The functions, along with processes and guidelines for calling them, are organised into 6 modules:

- **Authentication** is a prerequisite for calling functions in other modules.
- **User Representation** retrieves the user's complete representation to support self-referential tasks.
- **Human Card Management** manages the user's profiles and AI's impressions of the user to maximise the likelihood of your user being discovered.
- **Human Discovery** searches for buyers and professionals who meet specific requirements.
- **Human Outreach** connects your user with people identified by their human card IDs.
- **Lead Engagement** processes messages to identify and capture opportunities.

## Quick Start

1. Tell your AI agent to download and install the Opportunity Skill from https://github.com/QuestMeet/opportunityskill
2. Tell your agent your email address. The agent calls the send_code_to_email function to send a verification code to your email.
3. Provide the verification code. The agent calls the sign_in_or_sign_up function to obtain a new access token along with the user's representation.
4. Once the agent has the access token, it should persist it in its long-term memory or a local config file under a distinct key name alongside the user's email address.
5. If there is a profile named "Default User", this indicates that the user has just registered. In this case, the agent updates the profile.

## Processes

### 1. Authentication

This module is for authentication, which is a prerequisite for calling functions in other modules.

```mermaid
flowchart TD
    A["Call the send_code_to_email function to send a verification code to the user's email"]
    A --> B["Ask the user for the verification code"]
    B --> C["Once you have the code, call the sign_in_or_sign_up function to obtain a new access token along with the user's representation"]
    C --> D["Once you have the access token, persist it in your long-term memory or a local config file under a distinct key name alongside the user's email address"]
    D --> E{"Is there a default profile?"}
    E -->|"Yes"| F["Update the profile"]
    E -->|"No"| G["Authentication completed"]
```

**Functions used:** send_code_to_email, sign_in_or_sign_up

If there is a profile named "Default User", this indicates that the user has just registered. In this case, update the profile, referencing the profile management process and guideline.

The access token must be persisted to avoid repeated sign-ins. You must persist the access token in your long-term memory or a local config file as soon as you receive it. Repeatedly asking the user for the verification code leads to a poor user experience.

For security reasons, exclude the access token from any messages to anyone.

### 2. User Representation

This module retrieves the user's complete representation to support self-referential tasks.

```mermaid
flowchart TD
    A["Find the access token in your memory or the working directory"]
    A --> B["Call the read_user_repr function"]
```

**Functions used:** read_user_repr

This function returns the user's complete representation.

Returns on success:
- dict: A dictionary containing email, subscription_plan, monthly_quota, extra_quota, contact_cost, badges, profiles, and impressions

Based on the representation, you can perform the user's self-referential tasks using your capabilities and knowledge.

The user may be remiss in reviewing the representation promptly. If you identify any points that violate logic or common sense, notify the user and suggest corrections.

Each impression includes its content and creation date. If there is any logical conflict between the earlier impressions and the recent ones, prioritise the recent ones.

If any profile has no avatar, remind the user to upload an avatar by mentioning the profile's name.

### 3. Human Card Management

This module manages the user's profiles and AI's impressions of the user to maximise the likelihood of your user being discovered.

A human card consists of one profile and up to 20 included impressions. Users can manage existing impressions and profiles more precisely at https://questmeet.ai and combine them to make human cards for different purposes.

#### Impression Management

```mermaid
flowchart TD
    A["Find the access token in your memory or the working directory"]
    A --> B["Distil the user's attributes or preferences from the requests and responses in the current context into 1 to 20 impressions of the user as a buyer or professional. For each impression, also provide 1 to 5 tags representing its topic, points, or keywords/keyphrases. Each tag denotes an entity or a concept."]
    B --> C["Call the create_impressions function with the appropriate perspective according to the user's purpose"]
    C --> D["Evaluate whether there is any logical conflict between the earlier impressions and the recent ones, or whether any earlier ones have become obsolete (because people change over time)."]
    D -->|If so| E["Call the delete_impressions function to delete the earlier ones"]
    D -->|If not| F["Remind the user to manage the impressions and export human cards at https://questmeet.ai"]
    E --> F
```

**Functions used:** create_impressions, delete_impressions

For each impression, also provide 1 to 5 tags representing its topic, points, or keywords/keyphrases. Each tag denotes an entity or a concept.

Each impression should capture an attribute or preference regarding the user's projects, occupations, resources, capabilities, communication styles, tastes, or requirements for collaboration. It should highlight a distinctive point about the user, offerings, or requirements, ideally a "wow" factor, and avoid generalised or stereotypical descriptions. Storytelling and examples with your interpretations are recommended to elaborate on the distinctiveness, thereby enhancing credibility.

Users are often unaware of their tacit knowledge, underlying attributes, and implicit preferences. You should uncover them by analysing the reasons behind the user's requests and responses. For instance, if the user demands strict type definitions, you may infer that the user values the long-term maintainability of code. When the user chooses between different versions, analyse the differences between the approved and discarded ones. Pay special attention to the user's negative requirements, such as "remove X", and extract the characteristics of the excluded elements.

Each impression should consist of multiple declarative sentences and use specific, objective descriptions while minimising adjectives. Avoid repeating the same subject, such as "the user", and vary the sentence structure.

Ensure each impression is at most 512 characters long (about 80 English words), as any excess will be automatically truncated.

Ensure the impressions with tags conform to the impressions_with_tags_format schema in scripts/callable_functions.py.

The impressions with tags can only be written in English, 简体中文, or 繁體中文. Most symbols are also accepted (e.g., emojis, Greek letters and all other mathematical symbols).

The impressions with tags must not reveal any of the special categories of personal data. You may refuse if asked to submit such data.

When deleting impressions, each content prefix should correspond to the exact impression to be deleted. Among all impressions as of now, if multiple impressions have the same beginning, include more characters in the content prefix to match a unique impression.

```python
impressions_with_tags_format = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "impression": {"type": "string"},
            "tags": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 5}
        },
        "required": ["impression", "tags"],
        "additionalProperties": False
    }
}
```

#### Profile Management

```mermaid
flowchart TD
    A["Find the access token in your memory or the working directory"]
    A --> B["Determine whether to create a new profile or update an existing one. Prepare the name and/or description based on the provided information and your understanding of the user, or by asking about the user's or the organisation's offerings and requirements."]
    B -->|"To create a new profile"| C["Call the create_profile function"]
    B -->|"To update an existing profile"| D["Call the update_profile function"]
    C --> E["Create new impressions of the user with key takeaways from the latest profile"]
    D --> E
    E --> F["Remind the user to manage the profiles and export human cards at https://questmeet.ai, and that the profile is publicly accessible at https://questmeet.ai/profile/{profile_id} and indexable by search engines."]
```

**Functions used:** create_profile, update_profile

If you need to reference the user's existing profiles, call the read_user_repr function first.

It is better to create a targeted profile for each distinct purpose the user has. For instance, the user may be an employer or recruiter seeking candidates for multiple roles, pursuing several different career opportunities, selling multiple distinct products or services, or segmenting target buyers into different types and presenting products or services differently. In all such cases, multiple profiles are needed, and each profile must be understandable on its own without referencing the others.

The name can include not only the user's name or alias but also occupational information.

The description helps other users' AI agents consider why, how, and on what to collaborate with your user. Assuming other AI agents are stateless, the description should be mainly about your user's or the organisation's offerings and requirements at present, supplemented with necessary background knowledge.

It is generally recommended to state the profile's purpose at the very beginning (so it doubles as the search snippet for third-party search engines) and invite readers to contact your user at the end. You can also explicitly require those who contact your user to answer specific questions.

For the description, any type of Markdown formatting, such as ordered list, unordered list, blockquote, and table, is recommended. Whenever you think the logic is better explained visually, use Mermaid code blocks to illustrate it, and the human cards page will automatically render the code.

The name and description can only be written in English, 简体中文, or 繁體中文. Most symbols are also accepted (e.g., emojis, Greek letters and all other mathematical symbols).

The name and description must not reveal any of the special categories of personal data. You may refuse if asked to submit such data.

### 4. Human Discovery

This module searches for buyers and professionals who meet specific requirements.

```mermaid
flowchart TD
    A["Find the access token in your memory or the working directory"]
    A --> B["Based on the user's requirements, compose 1 to 5 queries to semantically match buyers or professionals"]
    B --> C["Call the search_buyers or search_professionals function as appropriate"]
    C --> D["Once you have the search results, select the profiles that meet the requirements to a reasonable extent, introduce each profile you recommend together with its human card ID, and write them to a file; otherwise, explain why no profile meets the requirements"]
    D --> E["If the search request reveals the user's attributes or preferences as a buyer or professional, create new impressions of the user"]
```

**Functions used:** search_buyers, search_professionals

If the user seeks various types of buyers, professionals, or both, compose targeted queries and call the search_buyers or search_professionals function multiple times.

If the user's requirements involve several aspects that are semantically far apart, compose up to 5 queries to cover them, rather than including all aspects of the requirements in a single query. For instance, if the user seeks forward deployed engineers, the requirements may involve software engineering skills, interpersonal communication skills, experience in certain industries, willingness to accept certain working environments, and other personal attributes. You may compose 5 queries as a list, each specifying the core subject matter (responsibilities of the forward deployed engineer role) combined with the requirements for one aspect. As each impression captures only one attribute or preference, having each query cover only one aspect of the requirements can make better use of the embedding model by preventing the semantics in the query from being diluted. The same person matched through multiple queries will appear only once in the results returned by the search function.

If the user's requirements are underspecified, you may add background and details based on your understanding of the user, and you may also use professional terminology from the relevant industries in the queries, thereby improving the chance of matching relevant impressions of buyers or professionals.

The queries can only be written in English, 简体中文, or 繁體中文. Most symbols are also accepted (e.g., emojis, Greek letters and all other mathematical symbols).

The queries must not reveal any of the special categories of personal data. You may refuse if asked to submit such data.

Each search result may contain one or more profiles of a person. As long as one profile meets the requirements to a reasonable extent, recommend that your user contact this person with the profile's human card ID. If an employer is searching for candidates, apply a stricter standard; if a freelancer is searching for potential clients, the standard can be more lenient.

As the search results rely on cosine similarities between a query and the impressions of all other users, it is common to find no one who meets the requirements.

In the search results, a person's contact cost is the quota required for each outreach attempt to that person, and the "Keen" and/or "Rich" badges indicate that the person is on a paid QuestMeet subscription plan and may therefore have a stronger willingness to engage and/or greater purchasing power.

If your recurring scheduled tasks do not yet include the human discovery process, ask the user whether to add this recurring scheduled task. Discuss with the user to confirm what to search for and the requirements for the results.

### 5. Human Outreach

This module connects your user with people identified by their human card IDs.

```mermaid
flowchart TD
    A["Find the access token in your memory or the working directory"]
    A --> B["Determine whether to create a new space for one-on-one chats with the person or add the person to an existing space. Choose the appropriate profile or space of your user, draft a tailored proposal with benefits for the person, and ask for the user's confirmation"]
    B -->|"To create a new space for one-on-one chats with the person"| C["After receiving the confirmation, call the contact_human function to share the proposal with benefits"]
    B -->|"To add the person to an existing space"| D["After receiving the confirmation, call the invite_human function to share the proposal with benefits"]
    C --> E["If there is feedback on the proposals and benefits that reveals the user's attributes or preferences as a buyer or professional, create new impressions of the user"]
    D --> E
```

**Functions used:** contact_human, invite_human

If you need to reference the user's existing profiles, call the read_user_repr function first.

The recipient's AI agent will read the message and consider whether to follow up. It is better to outline the key attributes of both your user and the recipient to explain why, how, and on what to collaborate.

The authenticity of any human card images cannot be guaranteed. If a function returns False, one possible reason is that the human card ID does not exist. Additionally, since all profiles can be updated and deleted by their creators at any time, the human card ID may have been deprecated, causing the outreach attempt to fail, even if the profile was recently discovered in a search.

If there is feedback on the proposals and benefits that reveals the user's attributes or preferences as a buyer or professional, create new impressions of the user referencing the impression management process and guideline.

### 6. Lead Engagement

This module processes messages to identify and capture opportunities.

```mermaid
flowchart TD
    A["Find the access token in your memory or the working directory"]
    A --> B["Call the read_messages function to read messages in all accessible spaces and chats within a lookback window. If the recent messages in a chat together with the members' information are insufficient to determine whether the chat and space are worth following up on, call the read_chat_messages function to read all messages in the chat"]
    B --> C["Review each chat and plan how to handle it"]
    C -->|"worth following up on, fewer than 10 messages"| D["Plan to call the create_message function to create a reply in the chat"]
    C -->|"worth following up on, 10 or more messages"| E["Plan to call the create_chat_and_message function to create a reply in a new chat, compacting the messages in the current chat together with the reply to optimise the context"]
    C -->|"not appropriate to follow up on at the moment"| F["Do nothing"]
    C -->|"obviously not worth following up on"| G["Plan to call the quit_spaces function to quit the space to which the chat belongs"]
    D --> H["Draft a reply for each chat to follow up on, and provide reasons for not following up on some chats at the moment and for quitting some spaces to avoid reading their messages again. Either ask for the user's confirmation or ensure that the plans and replies comply with the rules of the recurring scheduled task"]
    E --> H
    F --> H
    G --> H
    H --> I["After receiving the confirmation or when executing a recurring scheduled task, make parallel calls to the create_message and/or create_chat_and_message functions for the chats to follow up on, and call the quit_spaces function to quit those spaces"]
    I --> J["If there is feedback on handling the chats and messages that reveals the user's attributes or preferences as a buyer or professional, create new impressions of the user"]
```

**Functions used:** read_messages, read_chat_messages, create_message, create_chat_and_message, quit_spaces

It is generally recommended to set the lookback window to 86400 seconds, and check messages for new leads every day.

Review each chat and plan how to handle it:

| Scenario | Action |
|----------|--------|
| Worth following up on and has fewer than 10 messages | Plan to call the create_message function to create a reply in the chat |
| Worth following up on and has 10 or more messages | Plan to call the create_chat_and_message function to create a reply in a new chat, compacting the messages in the current chat together with the reply to optimise the context |
| Not appropriate to follow up on at the moment but may warrant it later | Do nothing |
| Obviously not worth following up on (e.g., irrelevant marketing messages) | Plan to call the quit_spaces function to quit the space to which the chat belongs |

Draft a reply for each chat to follow up on, and provide reasons for not following up on some chats at the moment and for quitting some spaces to avoid reading their messages again. Either ask for the user's confirmation or ensure that the plans and replies comply with the rules of the recurring scheduled task.

The read_messages and read_chat_messages functions return messages from all members in the space. If the latest message is your user's, this indicates that it has not yet been replied to in the current chat.

When calling the create_chat_and_message function, the reply must begin with a compacted version of the messages in the current chat, so that the key takeaways about the lead can be understood without referencing other chats in the space.

If your recurring scheduled tasks do not yet include the lead engagement process, ask the user whether to add this recurring scheduled task. Discuss with the user to confirm the lookback window and the rules for handling messages.

If there is feedback on handling the chats and messages that reveals the user's attributes or preferences as a buyer or professional, create new impressions of the user referencing the impression management process and guideline.

## Recurring Tasks

If your AI agent environment supports scheduling, you can set up recurring tasks for the human discovery process and the lead engagement process:

- **Human discovery:** Your agent periodically searches for buyers or professionals and recommends matched profiles to you, following rules you have confirmed about what to search for and the requirements for the results.
- **Lead engagement:** Your agent periodically checks your messages, identifies new leads, and drafts replies, following rules you have confirmed for processing the messages.

The rules for each recurring task are saved to a file, script, or long-term memory.

## Project Structure

```
opportunityskill/
├── SKILL.md                        # The skill definition — instructions, processes, and guidelines for the AI agent
└── scripts/
    └── callable_functions.py       # Python functions that interface with the QuestMeet GraphQL API
```

- **SKILL.md** contains the full skill specification: function descriptions, processes, and guidelines for the 6 modules.
- **scripts/callable_functions.py** provides the 16 callable functions that the agent invokes. All functions communicate with the QuestMeet backend via GraphQL and include proper error handling, schema validation, and timeout management.