<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Studio 10.0 | Multi-Modal Interface</title>
    <style>
        :root {
            /* Color Palette - Modern Dark AI Theme */
            --bg-body: #0f1117;
            --bg-sidebar: #161b22;
            --bg-card: #21262d;
            --bg-input: #0d1117;
            --accent-primary: #58a6ff;
            --accent-secondary: #238636;
            --text-main: #c9d1d9;
            --text-muted: #8b949e;
            --border-color: #30363d;
            --shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
            --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            --radius: 8px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-family);
            background-color: var(--bg-body);
            color: var(--text-main);
            height: 100vh;
            display: flex;
            overflow: hidden;
        }

        /* --- Sidebar --- */
        aside {
            width: 260px;
            background-color: var(--bg-sidebar);
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            padding: 1rem;
            transition: transform 0.3s ease;
            z-index: 100;
        }

        .brand {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 2rem;
            padding: 0.5rem;
        }

        .brand svg {
            fill: var(--accent-primary);
            width: 24px;
            height: 24px;
        }

        .nav-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 12px;
            border-radius: var(--radius);
            cursor: pointer;
            color: var(--text-muted);
            transition: background 0.2s, color 0.2s;
            margin-bottom: 4px;
            font-size: 0.95rem;
        }

        .nav-item:hover {
            background-color: var(--bg-card);
            color: var(--text-main);
        }

        .nav-item.active {
            background-color: rgba(88, 166, 255, 0.1);
            color: var(--accent-primary);
            font-weight: 600;
        }

        .nav-item svg {
            width: 18px;
            height: 18px;
            fill: currentColor;
        }

        .sidebar-footer {
            margin-top: auto;
            border-top: 1px solid var(--border-color);
            padding-top: 1rem;
            font-size: 0.8rem;
            color: var(--text-muted);
        }

        /* --- Main Content --- */
        main {
            flex: 1;
            display: flex;
            flex-direction: column;
            position: relative;
            background: radial-gradient(circle at top right, #1c2128 0%, #0f1117 40%);
        }

        header {
            padding: 1rem 2rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: rgba(15, 17, 23, 0.8);
            backdrop-filter: blur(10px);
        }

        h1 {
            font-size: 1.1rem;
            font-weight: 600;
        }

        .status-badge {
            background-color: rgba(35, 134, 54, 0.2);
            color: #3fb950;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .status-dot {
            width: 8px;
            height: 8px;
            background-color: #3fb950;
            border-radius: 50%;
            box-shadow: 0 0 8px #3fb950;
        }

        /* --- Views --- */
        .view-container {
            flex: 1;
            display: none; /* Hidden by default */
            flex-direction: column;
            overflow: hidden;
            padding: 0;
        }

        .view-container.active {
            display: flex;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(5px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* --- Chat View --- */
        .chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 2rem;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            scroll-behavior: smooth;
        }

        .message {
            display: flex;
            gap: 1rem;
            max-width: 800px;
            margin: 0 auto;
            width: 100%;
        }

        .avatar {
            width: 36px;
            height: 36px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            font-size: 1.2rem;
        }

        .avatar.user { background-color: var(--bg-card); border: 1px solid var(--border-color); }
        .avatar.ai { background-color: var(--accent-primary); color: white; }

        .message-content {
            background-color: transparent;
            padding-top: 6px;
            line-height: 1.6;
            font-size: 0.95rem;
        }

        .message-content strong {
            color: var(--text-main);
            display: block;
            margin-bottom: 4px;
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .input-zone {
            padding: 1.5rem 2rem;
            background-color: var(--bg-body);
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: center;
        }

        .input-wrapper {
            position: relative;
            width: 100%;
            max-width: 800px;
        }

        .chat-input {
            width: 100%;
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 1rem 3rem 1rem 1rem;
            border-radius: var(--radius);
            font-family: inherit;
            font-size: 1rem;
            resize: none;
            height: 60px;
            outline: none;
            transition: border-color 0.2s;
        }

        .chat-input:focus {
            border-color: var(--accent-primary);
        }

        .send-btn {
            position: absolute;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            cursor: pointer;
            color: var(--accent-primary);
            padding: 8px;
            border-radius: 4px;
        }

        .send-btn:hover {
            background-color: rgba(88, 166, 255, 0.1);
        }

        /* --- Image View --- */
        .image-controls {
            padding: 2rem;
            display: flex;
            justify-content: center;
            border-bottom: 1px solid var(--border-color);
        }

        .image-prompt-box {
            width: 100%;
            max-width: 800px;
            display: flex;
            gap: 10px;
        }

        .generate-btn {
            background-color: var(--accent-primary);
            color: white;
            border: none;
            padding: 0 24px;
            border-radius: var(--radius);
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .generate-btn:hover {
            background-color: #4094ea;
        }
        
        .generate-btn:disabled {
            background-color: var(--text-muted);
            cursor: not-allowed;
        }

        .gallery {
            flex: 1;
            overflow-y: auto;
            padding: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
            align-content: start;
        }

        .gallery-item {
            background-color: var(--bg-card);
            border-radius: var(--radius);
            overflow: hidden;
            border: 1px solid var(--border-color);
            animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            group: hover;
        }

        @keyframes popIn {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }

        .gallery-item img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            display: block;
        }

        .gallery-info {
            padding: 10px;
            font-size: 0.8rem;
            color: var(--text-muted);
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .loading-spinner {
            border: 3px solid rgba(255,255,255,0.1);
            border-top: 3px solid var(--accent-primary);
            border-radius: 50%;
            width: 24px;
            height: 24px;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* --- Toast Notification --- */
        .toast-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 1000;
        }

        .toast {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 12px 16px;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.9rem;
            animation: slideIn 0.3s ease;
            min-width: 250px;
        }

        .toast.success { border-left: 4px solid var(--accent-secondary); }
        .toast.info { border-left: 4px solid var(--accent-primary); }

        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        /* Responsive */
        @media (max-width: 768px) {
            aside {
                position: fixed;
                height: 100%;
                transform: translateX(-100%);
            }
            aside.open {
                transform: translateX(0);
            }
            .menu-toggle {
                display: block;
                margin-right: 10px;
                cursor: pointer;
            }
        }
        
        @media (min-width: 769px) {
            .menu-toggle { display: none; }
        }
    </style>
</head>
<body>

    <!-- Sidebar -->
    <aside id="sidebar">
        <div class="brand">
            <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
            NEXUS AI
        </div>

        <nav>
            <div class="nav-item active" onclick="switchTab('chat', this)">
                <svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z"/></svg>
                Smart Chat
            </div>
            <div class="nav-item" onclick="switchTab('image', this)">
                <svg viewBox="0 0 24 24"><path d="M21 19V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2zM8.5 13.5l2.5 3.01L14.5 12l4.5 6H5l3.5-4.5z"/></svg>
                Image Generator
            </div>
            <div class="nav-item" onclick="showToast('Settings panel is locked in Demo Mode.', 'info')">
                <svg viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L3.16 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>
                Settings
            </div>
        </nav>

        <div class="sidebar-footer">
            <p>NEXUS AI v10.0</p>
            <p style="opacity: 0.6; margin-top: 4px;">Frontend Simulation</p>
        </div>
    </aside>

    <!-- Main Content -->
    <main>
        <header>
            <div style="display:flex; align-items:center;">
                <div class="menu-toggle" onclick="toggleSidebar()">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
                </div>
                <h1 id="page-title">Smart Chat</h1>
            </div>
            <div class="status-badge">
                <div class="status-dot"></div>
                System Online
            </div>
        </header>

        <!-- Chat View -->
        <section id="view-chat" class="view-container active">
            <div class="chat-area" id="chat-history">
                <!-- Welcome Message -->
                <div class="message">
                    <div class="avatar ai">AI</div>
                    <div class="message-content">
                        <strong>NEXUS AI</strong>
                        Hello! I am your Multi-Modal Assistant. I can help you with coding, writing, and analysis. Switch to the "Image Generator" tab to create visuals.
                    </div>
                </div>
            </div>
            <div class="input-zone">
                <div class="input-wrapper">
                    <input type="text" id="user-input" class="chat-input" placeholder="Type your message here..." autocomplete="off">
                    <button class="send-btn" onclick="sendMessage()">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
                    </button>
                </div>
            </div>
        </section>

        <!-- Image View -->
        <section id="view-image" class="view-container">
            <div class="image-controls">
                <div class="image-prompt-box">
                    <input type="text" id="image-prompt" class="chat-input" placeholder="Describe the image you want to generate..." style="height:auto;">
                    <button class="generate-btn" id="gen-btn" onclick="generateImage()">
                        <span>Generate</span>
                    </button>
                </div>
            </div>
            <div class="gallery" id="image-gallery">
                <!-- Images will appear here -->
                <div class="gallery-item" style="display:flex; align-items:center; justify-content:center; height:200px; background: var(--bg-card); border:1px dashed var(--border-color);">
                    <p style="color:var(--text-muted)">No images generated yet.</p>
                </div>
            </div>
        </section>
    </main>

    <!-- Toast Notifications -->
    <div class="toast-container" id="toast-area"></div>

    <script>
        // --- State Management ---
        const state = {
            currentTab: 'chat',
            isGenerating: false
        };

        // --- Navigation ---
        function switchTab(tabId, navElement) {
            // Update UI State
            state.currentTab = tabId;
            
            // Update Nav Styling
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            navElement.classList.add('active');

            // Update View Visibility
            document.querySelectorAll('.view-container').forEach(el => el.classList.remove('active'));
            document.getElementById(`view-${tabId}`).classList.add('active');

            // Update Header Title
            const titles = { 'chat': 'Smart Chat', 'image': 'Image Generator' };
            document.getElementById('page-title').innerText = titles[tabId];
            
            // Close sidebar on mobile after selection
            if(window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('open');
        }

        // --- Chat Functionality ---
        const chatInput = document.getElementById('user-input');
        const chatHistory = document.getElementById('chat-history');

        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });

        function sendMessage() {
            const text = chatInput.value.trim();
            if (!text) return;

            // Add User Message
            appendMessage('user', text);
            chatInput.value = '';

            // Simulate AI Delay & Response
            setTimeout(() => {
                const response = getSimulatedResponse(text);
                appendMessage('ai', response);
            }, 1000 + Math.random() * 1000); // Random delay 1-2s
        }

        function appendMessage(role, text) {
            const msgDiv = document.createElement('div');
            msgDiv.className = 'message';
            
            const avatarDiv = document.createElement('div');
            avatarDiv.className = `avatar ${role}`;
            avatarDiv.innerText = role === 'user' ? 'U' : 'AI';

            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.innerHTML = `<strong>${role === 'user' ? 'You' : 'NEXUS AI'}</strong>${text}`;

            msgDiv.appendChild(avatarDiv);
            msgDiv.appendChild(contentDiv);
            
            chatHistory.appendChild(msgDiv);
            
            // Scroll to bottom
            chatHistory.scrollTop = chatHistory.scrollHeight;
        }

        function getSimulatedResponse(input) {
            input = input.toLowerCase();
            if (input.includes('hello') || input.includes('hi')) return "Hello! How can I assist you today?";
            if (input.includes('image') || input.includes('picture')) return "I can help you with that! Please switch to the 'Image Generator' tab to create visuals.";
            if (input.includes('code')) return "I'm ready to write code. Are you looking for Python, JavaScript, or perhaps HTML/CSS for Streamlit?";
            if (input.includes('streamlit')) return "Streamlit is a great framework for Python web apps. This interface you are using is a simulation of that architecture.";
            return "That's an interesting topic. Since I am currently running in 'Front-End Simulation Mode', I have a limited knowledge base, but I can simulate chat interactions effectively.";
        }

        // --- Image Generation Functionality ---
        const imgInput = document.getElementById('image-prompt');
        const gallery = document.getElementById('image-gallery');
        const genBtn = document.getElementById('gen-btn');

        imgInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') generateImage();
        });

        function generateImage() {
            const prompt = imgInput.value.trim();
            if (!prompt) {
                showToast("Please enter a description first.", "info");
                return;
            }

            if (state.isGenerating) return;
            state.isGenerating = true;

            // Clear initial empty state if present
            if (gallery.children.length === 1 && gallery.children[0].innerText.includes('No images')) {
                gallery.innerHTML = '';
            }

            // UI Feedback
            genBtn.disabled = true;
            genBtn.innerHTML = '<div class="loading-spinner" style="width:16px; height:16px;"></div>';
            
            // Simulate Generation Time
            setTimeout(() => {
                // Create Image Card
                const seed = Math.floor(Math.random() * 10000);
                // Using picsum.photos to simulate generated image based on seed
                const imageUrl = `https://picsum.photos/seed/${seed}/400/400`;
                
                const item = document.createElement('div');
                item.className = 'gallery-item';
                item.innerHTML = `
                    <img src="${imageUrl}" alt="${prompt}" loading="lazy">
                    <div class="gallery-info">
                        <span>${prompt.substring(0, 20)}...</span>
                        <span style="cursor:pointer" onclick="downloadImage('${imageUrl}')">⬇</span>
                    </div>
                `;

                // Insert at top
                gallery.insertBefore(item, gallery.firstChild);

                // Reset UI
                imgInput.value = '';
                genBtn.disabled = false;
                genBtn.innerHTML = '<span>Generate</span>';
                state.isGenerating = false;
                showToast("Image generated successfully!", "success");

            }, 2500); // 2.5s simulated delay
        }

        function downloadImage(url) {
            showToast("Image download started...", "info");
            // Real download logic would go here
            // In a real app, this would trigger a file save
        }

        // --- Toast System ---
        function showToast(message, type = 'info') {
            const container = document.getElementById('toast-area');
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            
            let icon = type === 'success' ? '✓' : 'ℹ';
            
            toast.innerHTML = `<span>${icon}</span> ${message}`;
            container.appendChild(toast);

            // Remove after 3 seconds
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(100%)';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

    </script>
</body>
</html>
