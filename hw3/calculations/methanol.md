<OpenMD version=2>
  <MetaData>

molecule {
  name = "methanol";
  atom[0] { type = "CT"; position( -5.96684, 1.08283, -0.00928);}
  atom[1] { type = "OH"; position( -4.93201, 2.04823, 0.02864);}
  atom[2] { type = "H1"; position( -5.60539, 0.17925, -0.5063);}
  atom[3] { type = "H1"; position( -6.826, 1.48931, -0.54848);}
  atom[4] { type = "H1"; position( -6.26343, 0.83944, 1.01366);}
  atom[5] { type = "HO"; position( -4.68999, 2.24405, -0.89252);}

  bond { members(1, 5); }
  bond { members(0, 3); }
  bond { members(0, 2); }
  bond { members(0, 1); }
  bond { members(0, 4); }

}


component{
  type = methanol;
  nMol = 1;
}

forceField = "Amber";

  </MetaData>
  <Snapshot>
    <FrameData>
        Time: 0
        Hmat: {{ 6.826, 0, 0 }, { 0, 2.24405, 0 }, { 0, 0, 1.90618 }}
    </FrameData>
    <StuntDoubles>
         0      pv           -5.96684            1.08283           -0.00928  0.000000e+00  0.000000e+00  0.000000e+00
         1      pv           -4.93201            2.04823            0.02864  0.000000e+00  0.000000e+00  0.000000e+00
         2      pv           -5.60539            0.17925            -0.5063  0.000000e+00  0.000000e+00  0.000000e+00
         3      pv             -6.826            1.48931           -0.54848  0.000000e+00  0.000000e+00  0.000000e+00
         4      pv           -6.26343            0.83944            1.01366  0.000000e+00  0.000000e+00  0.000000e+00
         5      pv           -4.68999            2.24405           -0.89252  0.000000e+00  0.000000e+00  0.000000e+00
    </StuntDoubles>
  </Snapshot>
</OpenMD>
