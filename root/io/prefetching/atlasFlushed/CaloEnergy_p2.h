//////////////////////////////////////////////////////////
//   This class has been generated by TFile::MakeProject
//     (Tue Jun 14 15:33:00 2011 by ROOT version 5.31/01)
//      from the StreamerInfo in file http://root.cern.ch/files/atlasFlushed.root
//////////////////////////////////////////////////////////


#ifndef CaloEnergy_p2_h
#define CaloEnergy_p2_h
class CaloEnergy_p2;

#include "Trk__EnergyLoss_p1.h"
#include "Riostream.h"
#include <vector>
#include "DepositInCalo_p2.h"

class CaloEnergy_p2 {

public:
// Nested classes declaration.

public:
// Data Members.
   Trk::EnergyLoss_p1 m_energyLoss;    //
   int                m_energyLossType;    //
   float              m_caloLRLikelihood;    //
   unsigned short     m_caloMuonIdTag;       //
   float              m_fsrCandidateEnergy;    //
   vector<DepositInCalo_p2> m_deposits;              //
   float                    m_etCore;                //

   CaloEnergy_p2();
   CaloEnergy_p2(const CaloEnergy_p2 & );
   virtual ~CaloEnergy_p2();

};
#endif
