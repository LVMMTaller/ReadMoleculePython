from rdkit import Chem

def read_smiles_from_csv(path):
    f = open(path,"r")

    f.readline()

    molLine = f.readline()
    mols = []
    while molLine:
        molLineS = molLine.split(",")
        mols.append(Chem.MolFromSmiles( molLineS[1]))
        molLine = f.readline()

    return mols

def read_sdf(path):
    inf = open(path, 'rb')
    fsuppl = Chem.ForwardSDMolSupplier(inf)

    mols = []
    for mol in fsuppl:
        if mol is None: continue
        mols.append(mol)
    return mols