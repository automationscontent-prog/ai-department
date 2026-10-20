# Origin conversation (2026-10-19)

This is where the idea started: Jerome talking it through with Claude. It's lightly edited. A side discussion on an unrelated topic and some personal planning notes were removed.

---

## Jerome: the local AI box

> Listen, in a world where AI is getting easier and easier to use, some people believe in a superintelligence threat, and some don't. In that world, companies do have a real privacy problem with AI, but they need AI.
>
> What do you think of a business that sells hardware and software, goes to see smallish companies, and sells them a rebranded Mac Mini? It has preinstalled software that helps them with the onboarding and set up local servers for their CRM, for their AI models, everything. It then basically has an AI that helps them set up the agents, so really, like an open-claw sort of simplified Grok bot with a mix of CRM, kind of like what I'm doing with the pit wall, but super easy.
>
> They buy the hardware, they pay for the software per month, and it helps them do the entire onboarding super easily. They have their own local AI server, and they have a bot that can help them build out tools when they need to. All run locally on their servers.
>
> What do you think about that business idea?

## Claude

The problem is real, but the business as described would be hard to run. A narrower version could work.

### What's right about it

- **Timing.** When OpenClaw blew up earlier this year, people literally bought Mac Minis just to run an agent. "An AI box in your office" is already an idea people understand.
- **Setup is the real pain.** Most business owners can't get agents working on their own. A done-for-you install is the kind of offer people pay for.
- **Hardware plus a monthly fee is sticky.** A box sitting in their office is harder to cancel than a SaaS login.

### Where it breaks

1. **"Local" and "builds your tools" pull against each other.** Models small enough to run on a Mac Mini are fine for searching documents, drafting emails and looking things up in a CRM. They're weakest at the part you're selling as the magic: an agent that builds tools when asked. Pit Wall (Jerome's personal AI dashboard) only works because it runs on Claude Opus. On a local model it would feel broken. So either the tool-builder is mediocre, or it quietly calls Claude or GPT and the privacy pitch is only half true.
2. **Most small companies don't feel the privacy problem.** They already run on Gmail, HubSpot, WhatsApp and ChatGPT. Privacy only makes people buy where it's a legal duty: lawyers, notaries, accountants, doctors, therapists, financial advisors, HR. For everyone else, the cloud companies' business plans that promise not to train on your data are private enough.
3. **You'd become an IT support company.** Boxes die. Backups, updates and new models land every month. Staff outside the office need remote access, and a local CRM is useless on a salesperson's phone without a VPN. On top of that, an agent with access to email and the CRM is a security risk, and OpenClaw's year has been a run of security incidents. If client data leaks, it leaked from your box.
4. **Rebranding a Mac Mini is awkward.** You can resell Macs with your software installed, but putting your own brand on Apple hardware runs into Apple's trademarks and reseller terms. The hardware margin is also thin. The money is in the setup fee and the monthly fee.
5. **Replacing their CRM is a migration project, not an install.** Plug into whatever they already use.

### The version that could work

- **One vertical where confidentiality is the law**, for example French accounting or law firms: "Your client files never leave the office."
- **Service first, box second.** Charge a setup fee plus a monthly fee, and have the client buy the hardware so you don't front any capital.
- **Be honest about the hybrid.** Sensitive data and search stay local. Heavy reasoning goes to a cloud model with no data retention, and you say so upfront.
- **Validate before buying anything.** Have 10 conversations with practice owners. If 3 are ready to pay, it's real. Purely as an illustration, 30 offices at €500 a month would be €15k MRR.

---

## Jerome: pairing it with the SaaS idea

> [...] just pair this local AI thing with an original idea that I had: to build a SaaS website.
>
> Small business owners take a subscription. On the onboarding, it asks them a bunch of questions, and then it continues to ask them questions in order to learn everything about the business. The model learns everything about the business: the marketing, the revenue, the sales processes, everything. Then it builds them a live top 5 list of AI tools to implement, constantly updating them with the top 5. If they click one, then it helps them download it for their business.
>
> The point is to address the sort of FOMO that people have, as well as the overwhelmingness. If you want to not fall behind your other competitor, you better use AI. At the same time, you can't follow all of AI. It's overwhelming. There's too much. That's the tool. Imagine that tool as a SaaS, with the installation of local servers as a whole sort of one business idea.

## Claude

Together, the two ideas are much stronger than either one alone. The SaaS fixes the box's biggest problem, which is how you find customers. But the money isn't where you think it is.

### What the pairing fixes

- **The SaaS becomes the box's funnel.** On its own, the box needs you visiting offices one by one. With the diagnostic in front, owners come in cheap, and the ones who need more get upsold.
- **It answers "what would I even use AI for?"** The top 5 list creates the reasons to buy the setup, and later the box.
- **The emotion is real.** "My competitor is using AI and I can't keep up" is a strong buying trigger, and "we keep you current so you don't have to follow AI" is a clear promise.

### Where it still breaks

1. **A list alone won't keep subscribers.** An owner sees their top 5, sets up one or two, and asks why they're still paying every month. A dentist's best tools don't change every week. Recommendations are information, and information products lose subscribers fast.
2. **ChatGPT and Claude already do the list.** Any owner can type "here's my business, which AI tools should I use?" and get a decent answer, often from an assistant that already knows their business. The big assistants keep adding exactly this.
3. **"Helps them download it" is where all the value and all the work are.** Most AI tools aren't downloads. They're sign-ups that then need hooking into the owner's email, CRM and data, plus training for the staff. That part is services, not software, and it's what people pay real money for.
4. **The two halves contradict each other.** A cloud SaaS that learns everything about the business, including revenue, sales and clients, collects exactly the sensitive data the box promises to protect.
5. **Owners won't answer endless questions.** Pull most of it from their tools instead (website, Gmail, Stripe, CRM) and ask only what's missing.

### The shape that would work

Call it an **"AI department" for one industry**:

1. **The diagnostic is free.** It takes 15 minutes, uses their connected tools and returns their personal top 5 with hours saved per week. It's a lead magnet, not the subscription.
2. **The setup is paid**, a fixed price for each tool you install.
3. **The monthly fee is upkeep.** You keep what you installed running, add new picks as they come out and train the staff. Being kept current is worth a monthly fee only when it's attached to things they actually use.
4. **The box is a premium tier**, only for clients whose confidentiality is a legal duty.

Stick to one industry. That's what makes this profitable. Within accountants, for example, the top 5 is about 80% the same for every firm, so you build each setup package once and sell it 50 times. Across all small businesses, every setup is custom and you're back to consulting by the hour.

The cheapest test: when a business owner asks what AI they should use, do the diagnosis by hand with Claude and quote them for setting up #1. Whether anyone pays is the first real signal.
