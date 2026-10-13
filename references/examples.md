# Before and after examples

Twenty-two vague comments next to rewrites that someone could act on. They cover reviews, 1:1s, peer feedback and promotion write-ups, mostly in the default SBI shape (Situation, Behavior, Impact, closing next step). Examples 21 and 22 show the STAR and four part formats.

How to read each one:

- **Before** is the vague original.
- **After** is the rewrite.
- **Impact** and **Next step** quote the exact phrases in the rewrite that state what changed and what to do next. The linter in `tests/lint_examples.py` checks that both appear.

All people, dates and numbers are illustrative. When using the skill on real feedback, never invent facts. Use placeholders such as [date] or [outcome] if the writer has not supplied them.

## Example 1: review, praise

**Before:** Priya is a rockstar and did a great job this year.

**After:** In March, Priya rewrote the deploy script after three failed releases in two weeks. Releases since then have gone out without a rollback, which gave the team back about four hours a week they had spent on manual fixes. Keep documenting changes the way you did in that PR, and consider walking the new hires through it in November.

- **Impact:** which gave the team back about four hours a week
- **Next step:** consider walking the new hires through it in November

## Example 2: review, criticism

**Before:** Marcus needs to show more ownership.

**After:** In the October incident, Marcus waited two days for the infra team to respond before escalating, and the customer fix slipped from Tuesday to Friday. I expected him to escalate on day one, since he had the authority and the contact. Starting next sprint, when a dependency is blocked for more than 24 hours, post it in the team channel and tag me.

- **Impact:** the customer fix slipped from Tuesday to Friday
- **Next step:** when a dependency is blocked for more than 24 hours, post it in the team channel and tag me

## Example 3: 1:1, direction

**Before:** You need to be more strategic.

**After:** In Thursday's roadmap review, your proposal listed 12 tasks but did not say which customer problem they solved, so the group spent 20 minutes asking. Open the next proposal with the problem, who has it, and what changes if we solve it, then list tasks. Try that on the Q1 draft and send it to me by Friday so we can compare.

- **Impact:** the group spent 20 minutes asking
- **Next step:** send it to me by Friday so we can compare

## Example 4: peer, conflict

**Before:** Dana is hard to work with.

**After:** In last week's design review, Dana interrupted me three times before I finished explaining the schema, and I stopped sharing my concerns about the migration. I would like her to let me finish a point before responding. If she wants to challenge it, I would welcome that in a comment on the doc after the meeting.

- **Impact:** I stopped sharing my concerns about the migration
- **Next step:** let me finish a point before responding

## Example 5: review, praise on communication

**Before:** Great communicator.

**After:** Jun's weekly update on the payments migration lists what shipped, what is at risk, and what he needs from others, in under 200 words. Two partner teams told me they stopped sending status pings because of it. Keep that format, and share the template with the other leads at the next staff meeting.

- **Impact:** Two partner teams told me they stopped sending status pings because of it
- **Next step:** share the template with the other leads at the next staff meeting

## Example 6: 1:1, quality

**Before:** Your work is sloppy.

**After:** Three of your last five pull requests failed CI on tests you did not run locally, and reviewers spent about 30 minutes each flagging the same lint errors. Before opening a PR, run the test suite and linter locally. I will check CI pass rates on your PRs with you in two weeks.

- **Impact:** reviewers spent about 30 minutes each flagging the same lint errors
- **Next step:** run the test suite and linter locally

## Example 7: promotion write-up

**Before:** Ready for senior. Strong technical skills and leadership.

**After:** Over the last two quarters, Amir led the search migration across 4 services, wrote the design doc that 3 teams signed off on, and mentored 2 engineers who each shipped their first feature on the project. The migration finished two weeks early and cut query latency from 800 ms to 300 ms. For the senior bar, the open gap is driving work outside his own team, so take the lead on the cross-team observability proposal in Q1.

- **Impact:** cut query latency from 800 ms to 300 ms
- **Next step:** take the lead on the cross-team observability proposal in Q1

## Example 8: peer, thanks

**Before:** Thanks for the help!

**After:** Thanks for staying 40 minutes after standup on Tuesday to walk me through the billing retry logic. I fixed the double-charge bug that afternoon, and 12 affected customers got refunds by Wednesday. I would like to pair with you on the next billing ticket.

- **Impact:** 12 affected customers got refunds by Wednesday
- **Next step:** pair with you on the next billing ticket

## Example 9: review, planning

**Before:** Needs to improve time management.

**After:** Four of the last six sprint commitments finished after the sprint ended, each by 2 to 3 days, because estimates were set before the dependency was confirmed. That pushed two releases and left QA with a compressed window. Next sprint, confirm each dependency before committing and flag any ticket where one is still open at planning.

- **Impact:** left QA with a compressed window
- **Next step:** confirm each dependency before committing

## Example 10: 1:1, praise on a presentation

**Before:** Good presentation.

**After:** In Wednesday's demo, you opened with the customer's 3 day wait time before showing the feature, and the VP asked for a pilot on the spot. Leading with the problem is what made it land. Do the same for the board prep next month.

- **Impact:** the VP asked for a pilot on the spot
- **Next step:** Do the same for the board prep next month

## Example 11: review, team dynamics

**Before:** Has a negative attitude.

**After:** In the last three retros, Sam answered new process proposals with "that will not work" before the proposer finished, and two teammates have since stopped bringing ideas to the retro. I would like him to ask one clarifying question before giving a verdict. Try it at Thursday's retro and I will give you notes afterward.

- **Impact:** two teammates have since stopped bringing ideas to the retro
- **Next step:** ask one clarifying question before giving a verdict

## Example 12: peer, documentation

**Before:** Your docs are confusing.

**After:** The setup guide for the auth service skips the step that creates the service account, and I lost about 90 minutes on Monday before finding it in Slack. Adding that step between sections 2 and 3 would fix it. I can open a PR for it if you prefer.

- **Impact:** I lost about 90 minutes on Monday
- **Next step:** Adding that step between sections 2 and 3

## Example 13: review, praise on a self-started fix

**Before:** Shows great initiative.

**After:** Leila noticed in August that on-call pages were up 40% after the config change and wrote the runbook without being asked. Pages dropped back to the earlier level within two weeks. Keep picking up gaps like this, and next quarter bring one to planning before starting it so we can size the effort.

- **Impact:** Pages dropped back to the earlier level within two weeks
- **Next step:** bring one to planning before starting it

## Example 14: 1:1, speaking up

**Before:** You are too quiet in meetings.

**After:** In the last four planning meetings you shared your view only when I asked you directly, and twice the concerns you raised afterward in Slack would have changed the plan. I would like to hear them in the room. Pick one meeting this week and state your top concern in the first ten minutes.

- **Impact:** twice the concerns you raised afterward in Slack would have changed the plan
- **Next step:** state your top concern in the first ten minutes

## Example 15: review, level expectations

**Before:** Not delivering at level.

**After:** The staff bar for this role includes setting technical direction across teams. This half, the 3 design docs Ravi wrote covered only his own team's services, and the platform team learned of the API change after it shipped. For the next cycle, send each design doc to the affected teams at least a week before review.

- **Impact:** the platform team learned of the API change after it shipped
- **Next step:** send each design doc to the affected teams at least a week before review

## Example 16: 1:1, praise on handling a customer

**Before:** Handled that well.

**After:** When the customer escalated on Friday, you acknowledged the miss in the first sentence, gave a fix date, and sent an update at noon as promised. The customer replied that they would stay through renewal. Use the same three steps next time: name the miss, give a date, send the update.

- **Impact:** The customer replied that they would stay through renewal
- **Next step:** name the miss, give a date, send the update

## Example 17: peer, code review tone

**Before:** Code review comments are harsh.

**After:** On PR 482, the comment "this is wrong, redo it" gave no reason or alternative, and the author asked me privately whether they should keep contributing. A comment that names the issue, the reason, and a suggested change would have worked better. Try that format on your next 3 reviews.

- **Impact:** the author asked me privately whether they should keep contributing
- **Next step:** Try that format on your next 3 reviews

## Example 18: review, mixed

**Before:** Strong technical skills but needs to work on stakeholder management.

**After:** Nina designed the caching layer that cut API costs by 22%. Her gap this half was the pricing change: she told product about it two days before launch, and they had to rewrite the customer email overnight. Share changes that touch customers as soon as the design is approved, and add product to the review invite.

- **Impact:** they had to rewrite the customer email overnight
- **Next step:** add product to the review invite

## Example 19: 1:1, praise on routine work

**Before:** Keep up the good work.

**After:** Your bug triage this month cut the open backlog from 140 to 85 tickets, and support stopped escalating the login issues after you labeled them by cause. Keep triaging on Mondays, and write down the labeling rules so someone can cover when you are out.

- **Impact:** support stopped escalating the login issues after you labeled them by cause
- **Next step:** write down the labeling rules so someone can cover when you are out

## Example 20: review, raising blockers

**Before:** Needs to be more proactive.

**After:** In the last three sprints, Omar raised blocked tickets only after I asked about them, and two of them sat idle for 4 and 6 days. Surface a blocker in standup the day it appears. I will check the board with you next Friday to see how it went.

- **Impact:** two of them sat idle for 4 and 6 days
- **Next step:** Surface a blocker in standup the day it appears

## Example 21: review, promotion story (STAR)

**Before:** Did a great job leading the migration.

**After:** In April, the billing service was failing its nightly sync about once a week, and Kofi was asked to own the move to the new queue. He split the work into 5 stages, ran each against a copy of production data, and held the cutover until the error rate stayed under 0.1% for three days. The sync has not failed since June, and support tickets about missing invoices dropped from 30 a month to 2. Next quarter, write up the staging approach as a runbook so other teams can reuse it.

- **Impact:** support tickets about missing invoices dropped from 30 a month to 2
- **Next step:** write up the staging approach as a runbook so other teams can reuse it
- **Format:** STAR

## Example 22: 1:1, missed handoff (four part)

**Before:** Communication around releases could be better.

**After:** Situation: in last Thursday's release, the config change shipped without a note to support. Behavior: you merged it after the review but did not post it in the release channel. Impact: support spent 2 hours on Friday answering customers about a setting they could not find. Next step: post every customer-visible change in the release channel before merging, starting with next week's release.

- **Impact:** support spent 2 hours on Friday answering customers about a setting they could not find
- **Next step:** post every customer-visible change in the release channel before merging, starting with next week's release
- **Format:** Four part
