import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UiService {
  private showSideMenu:boolean = false;
  private subject = new Subject<any>();

  constructor() { }

  toggleSideNav(): void {
    this.showSideMenu = !this.showSideMenu;
    this.subject.next(this.showSideMenu);
    console.log(`showSideMenu=${this.showSideMenu}`);
  }

  onToggle(): Observable<any>{
    return this.subject.asObservable();
  }
}
