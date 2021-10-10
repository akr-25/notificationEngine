import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from '../models/Users'
import { Observable } from 'rxjs';
import { BACKEND_URL } from '../urls';


const httpOptions = {
  headers: new HttpHeaders(
    {
      'Content-Type': 'application/json'
    }
  )
}


@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private users_url = `${BACKEND_URL}/users`;

  constructor(private http: HttpClient) { }

  
}
