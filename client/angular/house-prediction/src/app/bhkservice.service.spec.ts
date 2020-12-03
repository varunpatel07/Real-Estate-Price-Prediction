import { TestBed } from '@angular/core/testing';

import { BhkserviceService } from './bhkservice.service';

describe('BhkserviceService', () => {
  let service: BhkserviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BhkserviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
