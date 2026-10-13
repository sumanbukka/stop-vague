# stop-vague

Turn vague feedback into SBI or STAR feedback people can act on.

stop-slop and similar tools fix how writing sounds. stop-vague fixes whether feedback is useful, because most bad feedback is written by humans and sounds natural.

![A vague line is struck through, then the rewrite builds up in four parts: situation, behavior, impact and next step.](assets/demo.gif)

**Before**

> You need to be more strategic.

**After**

> In Thursday's roadmap review, your proposal listed 12 tasks but did not say which customer problem they solved, so the group spent 20 minutes asking. Open the next proposal with the problem, who has it, and what changes if we solve it, then list tasks. Try that on the Q1 draft and send it to me by Friday so we can compare.

"Needs to be more strategic" tells someone something is wrong and nothing about what to do on Monday. stop-vague finds the vague parts, asks for the missing facts, and rewrites the feedback around a real moment, a behavior, its impact, and a next step.

More pairs, covering reviews, 1:1s, peer feedback and promotion write-ups, are in [references/examples.md](references/examples.md).

It never invents facts. If you have not given it the example or the outcome, it asks, or leaves a marked placeholder like [date].

## Quick install

Copy this into your terminal (needs Node.js):

```sh
npx skills add sumanbukka/stop-vague --skill stop-vague --global --yes
```

Then ask your coding agent: `use stop-vague on this: <your feedback>`

It installs for the coding agents the CLI finds on your machine and copies the whole repo into the skill folder. Other tools and install methods are below.

## Use it in your tool

One source of truth (`SKILL.md`), built into the formats each tool wants.

| Tool | How |
| --- | --- |
| Claude Code | `curl -fsSL https://raw.githubusercontent.com/sumanbukka/stop-vague/main/scripts/install.sh \| bash` (add `-s -- --project` to install into the current repo instead). Then ask: `use stop-vague on this: ...` |
| Any coding agent | Paste this into the agent: `Install the /stop-vague skill globally from https://github.com/sumanbukka/stop-vague` |
| Skills CLI | See [Quick install](#quick-install) above. |
| Claude.ai and Claude Desktop | Download [dist/stop-vague.zip](dist/stop-vague.zip), then go to Customize, Skills, click +, Create skill, Upload a skill. Needs code execution and file creation enabled. Menu names change, so look for Skills if this has moved. |
| Claude Projects | Paste [dist/PROMPT.md](dist/PROMPT.md) into the project instructions. |
| ChatGPT | Paste [dist/PROMPT.md](dist/PROMPT.md) into Custom Instructions, or into the instructions of a Custom GPT. |
| Gemini | Paste [dist/PROMPT.md](dist/PROMPT.md) into a Gem's instructions. |
| Cursor | Copy [dist/stop-vague.mdc](dist/stop-vague.mdc) to `.cursor/rules/stop-vague.mdc`. |
| GitHub Copilot | Append the contents of [dist/PROMPT.md](dist/PROMPT.md) to `.github/copilot-instructions.md`. |
| Any API | Use [dist/PROMPT.md](dist/PROMPT.md) as the system prompt. |

## How to use it

Paste your feedback after one of these lines.

| You type | You get |
| --- | --- |
| `use stop-vague on this: <feedback>` | The default: scores, every vague phrase quoted, a rewrite, and a re-score. It asks for missing facts or leaves [placeholders]. |
| `use stop-vague on this, rewrite only: <feedback>` | Just the rewrite and one line on what changed. |
| `score this feedback, do not rewrite it: <feedback>` | The score table, the quoted violations and the facts a rewrite would need. |
| `use STAR for this: <feedback>` | The rewrite in STAR. Say it once and it holds for the conversation. Also `four part`. |

In Claude Code you can set the format once for a project with a line like `feedback format: STAR` in CLAUDE.md. SBI is the default.

## Formats

| Format | Shape | When |
| --- | --- | --- |
| SBI (default) | Situation, Behavior, Impact, then a closing next step | Most feedback |
| STAR | Situation, Task, Action, Result, then a closing next step | Promotion write-ups, self-reviews |
| Four part | Situation, Behavior, Impact, Next step | When you want the next step as its own part |

It does not ask which format to use. Say "use STAR" once and it holds for the conversation. In Claude Code you can also put a line like `feedback format: STAR` in CLAUDE.md.

## What it does

It scores your draft on five dimensions (specificity, behavior, impact, actionability, tone fit), quotes every vague phrase it finds, rewrites with the 8 rules applied, and scores again. Anything under 35 out of 50 gets rewritten.

The rules, the phrase list and the structural patterns are plain Markdown. Read them, fork them, change them to match how your team talks.

```
stop-vague/
  SKILL.md                 core instructions
  references/
    phrases.md             vague phrases and what to ask for instead
    structures.md          structural patterns that hide the message
    examples.md            22 before and after pairs
  dist/                    generated: PROMPT.md, stop-vague.mdc, stop-vague.zip
  scripts/build.py         builds dist/ from SKILL.md and references/
  scripts/install.sh       Claude Code installer
  tests/lint_examples.py   checks every example
```

## Privacy and data handling

- This project ships only prompt text (Markdown, plus files built from it). It has no server and no database, and it stores nothing.
- Feedback you paste goes only to the AI tool you already use, under that provider's terms. Check those terms for how your provider handles your data.
- Replace real names with placeholders such as [Name] before pasting, especially for sensitive topics like performance plans, compensation, or termination. The skill will remind you once if it sees a real name next to that kind of content, and then carry on.

## Contributing

Add a before and after to `references/examples.md` in the same format (an optional `Format:` line marks STAR or four part), then run:

```
python3 tests/lint_examples.py
python3 scripts/build.py
```

The lint fails if a rewrite contains a banned vague phrase, has no concrete anchor (a number, day or month), or if the Impact and Next lines do not appear in the rewrite. CI also fails if `dist/` is out of date, so always run the build before you commit.

Real examples from your own work, with names and numbers changed, are the most useful contribution.

## License

MIT
