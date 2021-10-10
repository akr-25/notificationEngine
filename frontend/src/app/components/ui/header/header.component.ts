import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { UiService } from '../../../services/ui.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  showSideMenu: boolean = false;
  subscription:Subscription;

  constructor(private uiservice: UiService) {
    this.subscription = this.uiservice.onToggle().subscribe((value)=>(this.showSideMenu = value));
   }

  ngOnInit(): void {
  }

  toggleSideMenu(){
    this.uiservice.toggleSideNav();
  }

}
