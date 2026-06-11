# JARVIS AI — End‑to‑End Overview (LinkedIn Video Script)

> Use this as your spoken script while showing the project video/screens.

---

## 0) Opening + Self‑Introduction (0:00–0:10)

Good evening / good morning everyone. I’m **Khanish**. Today, I built something new with AI—an interactive assistant I named **JARVIS**.

This project doesn’t just answer questions. It can **listen to you**, **understand what you want**, and then **help automate tasks** on your computer.

---

## 1) Why This Project Exists (0:10–0:25)

Most people know about AI chatbots—but not everyone has seen an AI system that can **work like a real assistant**:
- understand your intent,
- use tools,
- and take actions.

So in this short video, I’ll give you a simple, end‑to‑end overview of how it works.

---

## 2) What You’re Seeing on Screen (0:25–0:40)

When you run the project, you get a desktop UI.

On the right side you have a **command input**—you can type questions—or talk through the microphone.

On the left side, you can see an **interactive system monitor** and a “JARVIS core” style HUD that reflects states like:
- listening
- thinking
- speaking

---

## 3) Start the Project (Command + First Run) (0:40–1:00)

To start JARVIS, you run:

**`python main.py`**

The application launches the UI first, then it connects to the Gemini live AI session in the background.

---

## 4) Setup: Gemini API Key + OS Selection (1:00–1:35)

The first time you open it, you’ll see an initialization overlay.

You’ll provide:
1. **Your Gemini API key** (from Gemini Studio)
2. Your **operating system** selection

If you haven’t created an API yet, this is where you generate it in Gemini Studio, then paste it into the UI.

After that, the app stores it into `config/api_keys.json`, so you don’t need to do this every run.

---

## 5) Audio: Microphone + Speaker Configuration (1:35–2:15)

JARVIS uses real audio input and audio output.

I also built a complete audio device workflow so you can use:
- a headset microphone + headset output, **or**
- your system mic + system speakers.

### Audio setup utility
Run:

**`python audio_setup.py`**

This utility lets you:
- list audio devices,
- test the microphone,
- test speaker playback,
- and configure preferred devices.

In code, `config/audio_config.py` manages device detection and persistence.

### In the UI
Inside JARVIS, there are dropdowns labeled **INPUT** and **OUTPUT** so you can switch devices quickly.

---

## 6) The Core Idea: “AI + Tools” (2:15–2:55)

Now the most important part.

JARVIS is powered by **Gemini Live** with **tool calling**.

Instead of only generating text, it can decide to call functions like:
- open apps
- search the web
- read and process files
- control the browser
- set reminders
- play and summarize YouTube videos
- analyze the screen (vision)

That’s what makes it feel like an assistant, not just a chatbot.

---

## 7) How Commands Become Actions (2:55–3:45)

Here’s the simple flow:

1. You speak or type a command.
2. JARVIS listens, transcribes, and sends your request to Gemini.
3. Gemini returns either:
   - a direct spoken response, or
   - a **tool call**.
4. JARVIS executes the tool through the matching module inside `actions/`.

In `main.py`, you can see a tool execution dispatcher that maps tool names to real functions.

---

## 8) What JARVIS Can Do (Show Features) (3:45–5:10)

Now I’ll show the functionality categories.

### A) Automation on your computer
- Open applications
- Control browser actions
- Perform system actions like settings and desktop automation

### B) File understanding & processing
A key feature: you can **upload a file** and ask questions about it.

JARVIS can work with different file types using `file_processor`, such as:
- images, OCR, description
- PDFs, summarization and extraction
- code files, explanation and review
- spreadsheets and data formats

### C) Web and YouTube
JARVIS can also:
- do web search
- open YouTube and control video actions like play, summary, trending, and info

### D) Vision: “Tell me what’s on screen”
If you ask something like:
- “What do you see on my screen?”
- “Analyze this image/camera”

…it uses `screen_process` to capture and analyze.

Important note: after the vision tool is triggered, the vision module provides the response.

---

## 9) Memory: Learning Your Preferences (5:10–5:35)

JARVIS can also save important user context.

If you tell it things worth remembering—like preferences or long‑term details—it can store them in long‑term memory.

This helps make future conversations more personalized.

---

## 10) Closing + Call to Action (5:35–6:00)

So that’s my **JARVIS AI**—a tool‑calling, audio‑driven assistant that can interact with humans and automate real tasks.

If you liked this concept, make sure to check the repo, and feel free to share your feedback.

Thank you for watching.
