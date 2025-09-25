README.md
v6
# 🎶 AlatusAI Music Studio

AlatusAI Music Studio is a **chat-first, AI-driven music companion** that helps users generate, upload, and assemble studio-quality songs.

---

## ✨ Features
- 🎤 Generate stems (guitar, drums, vocals) via AI prompts  
- 🎶 Upload your own stems (MP3/WAV)  
- 📝 Select, combine, and preview stems  
- 🔊 One-click mix assembly with live audio playback  
- 🎨 Dark theme UI with TailwindCSS  

---

## 🛠️ Tech Stack
- **Frontend**: React (Vite) + TailwindCSS  
- **Backend**: Flask + Flask-Smorest + Flask-CORS  
- **Containerization**: Docker + docker-compose  
- **Demo Assets**: Static MP3 files in `/static/mock/`  

---

## 🚀 Run Locally
```bash
docker-compose up --build
```

Then open [http://localhost:5173](http://localhost:5173) for the frontend  
and [http://localhost:5000/docs](http://localhost:5000/docs) for the backend API docs.

---

## 🏗️ User Flow

1. **Chat Composer**: Enter a prompt describing your song (e.g. "Chill indie guitar riff with soft vocals").
2. **AI Stem Generation**: The app generates demo stems (guitar, drums, vocals) with sample metadata and playback links.
3. **Upload Stems**: Add your own MP3/WAV stems to the project.
4. **Select Stems**: Pick generated and/or uploaded stems for assembly.
5. **One-click Mix**: Assemble selected stems into a new track and preview with live audio.
6. **Download**: Save your mix for future use.

---

## 🎵 Demo Assets

Demo MP3 files are included for instant playback in your local environment:

- `backend/static/mock/guitar.mp3`
- `backend/static/mock/drums.mp3`
- `backend/static/mock/vocals.mp3`
- `backend/static/mock/mix.mp3`

You can swap these for your own samples!

---

## 🖼️ Screenshots & GIFs

![Prompt to Stems](demo/demo-2.png)

![Mix Preview](demo/demo-flow.gif)

---

## 🤝 Contributing

PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 💡 Inspiration

Built by [AlatusAI](https://github.com/AlatusAI) for musicians, creators, and AI music fans.
