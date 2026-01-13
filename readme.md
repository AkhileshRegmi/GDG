# Project Repository

This repository contains **two branches**, each dedicated to a separate task.

---

## 🔹 Branch: Backend-task1  
### Task 1: Productivity Management Dashboard API

A backend API for managing tasks and tracking user productivity.

**Key Features**
- JWT-based user authentication and authorization  
- CRUD operations for tasks (title, description, priority, status, deadline, tags)  
- Tasks linked to individual users  
- Automatic overdue task detection  
- Search and filtering by status, priority, deadline, and tags  
- Productivity analytics endpoints:
  - Tasks completed per day/week  
  - Created vs completed tasks  
  - Overdue task count  
  - Completion rate  

**Optional Enhancements**
- Recurring tasks  
- Notifications/reminders  
- Advanced analytics (average completion time, trends, common priorities)

**Constraints**
- Any backend framework and database  
- RESTful design, validation, error handling, and logging  

---

## 🔹 Branch: Python-task2  
### Task 2: Minimal IRC Client Implementation

A terminal-based IRC client built using raw sockets only.

**Key Features**
- TCP connection to a configurable IRC server, port, and channel  
- IRC handshake using `NICK` and `USER`  
- Handle core IRC commands: `PING/PONG`, `JOIN`, `PRIVMSG`, `QUIT`  
- Join one channel and exchange real-time messages  
- User commands:
  - `/join #channel`
  - `/quit`  
- Maintains client state (nickname, connection status, current channel)

**Constraints**
- No IRC libraries  
- Single server and single channel  
- No TLS, message history, or reconnection logic  

---
