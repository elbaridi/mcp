import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ChatMessage {
  content: string;
  isUser: boolean;
  timestamp: Date;
}

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = 'http://localhost:8066';

  constructor(private http: HttpClient) { }

  sendMessage(message: string): Observable<string> {
  const body = { query: message };
  return this.http.post(
    `${this.apiUrl}/chat/send`,
    body,
    {
      headers: { 'Content-Type': 'application/json' },
      responseType: 'text'
    }
  );
}
}
