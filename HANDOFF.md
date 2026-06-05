# HANDOFF

This file defines how work is handed off between agents in this repository.

## Goal

Enable fast agent switching without losing context, decisions, or next actions.

## Handoff Trigger

Create or update a handoff note when:

- A task is paused before completion.
- Ownership is intentionally switched to another agent.
- The current agent is blocked and needs another pass.

## Required Handoff Payload

Every handoff should include:

1. Task summary: one sentence on objective and status.
2. Scope: files touched and files intentionally not touched.
3. Changes made: concise bullets of what was done.
4. Validation: checks run, results, and any gaps.
5. Open issues: blockers, assumptions, and risks.
6. Next actions: ordered list of the next 1-3 steps.
7. CAP state: whether changes are committed/pushed.

## Recommended Format

Use this template in agent messages or notes:

```text
Handoff Summary:
- Objective:
- Status:

Scope:
- Touched:
- Untouched:

Changes:
- 

Validation:
- Commands:
- Results:
- Not run:

Open Issues:
- 

Next Actions:
1. 
2. 
3. 

CAP State:
- Commit: yes/no
- Push: yes/no
```

## Repository Conventions

- Use `uv` whenever possible for Python workflows.
- `CAP` means commit and push.

## Operational Note

When switching agents, paste the latest handoff block into the next agent prompt so it can continue without re-discovery.
