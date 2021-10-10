import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { UiService } from './services/ui.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  showSideMenu:boolean = false;
  subscription:Subscription;
  
  constructor(private uiservice: UiService) {
    this.subscription = this.uiservice.onToggle().subscribe((value)=>(this.showSideMenu = value));
  }

  title = 'frontend';
}
