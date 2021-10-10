import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { User } from '../../../models/Users'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  @Output() onLogIn: EventEmitter<User> = new EventEmitter();

  userid:string = "";
  password:string = "";

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit(){
    if(!this.userid){
      alert('Enter the user id please');
      return;
    }
    else if(!this.password){
      alert('Enter the password');
      return;
    }

    const newUser = {
      UserID: this.userid,
      password: this.password
    }

    this.userid = "";
    this.password = "";
  }

}
